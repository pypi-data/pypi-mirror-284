# ProtoTwin Gymnasium Environment

This package provides a base environment for [Gymnasium](https://gymnasium.farama.org/index.html), to be used for reinforcement learning.

## Introduction

ProtoTwin Connect allows external applications to issue commands for loading models, stepping the simulation and reading/writing signals. This package provides a base environment for Gymnasium, a library for reinforcement learning. ProtoTwin Connect is a drop-in replacement for existing physics libraries like PyBullet and MuJoCo. The advantage provided by ProtoTwin Connect is that you don't need to programatically create your robot/machine or start with an existing URDF file. Instead, you can import your CAD into ProtoTwin and, with a few clicks of the mouse, you can define rigid bodies, collision geometry, friction materials, joints and motors.

### Signals

Signals represent I/O for components defined in ProtoTwin. The [prototwin package](https://pypi.org/project/prototwin/) provides a client for starting and connecting to an instance of ProtoTwin Connect. Using this client you can issue commands to load a model, step the simulation forwards in time, read signal values and write signal values. Some examples of signals include:

* The current simulation time
* The target position for a motor
* The current velocity of motor
* The current force/torque applied by a motor
* The state of a volumetric sensor (blocked/cleared)
* The distance measured by a distance sensor
* The accelerations measured by an accelerometer

Signals are either readable or writable. For example, the current simulation time is readable whilst the target position for a motor is writable.

#### Types

Signals are strongly typed. The following value types are supported:

* Boolean
* Uint8
* Uint16
* Uint32
* Int8
* Int16
* Int32
* Float
* Double

You can find the signals provided by each component inside ProtoTwin under the I/O dropdown menu. The I/O window lists the name, address and type of each signal along with its access (readable/writable). Python does not natively support small integral types. The client will automatically clamp values to the range of the integral type. For example, attempting to set a signal of type Uint8 to the value 1000 will cause the value to be clamped at 255.

#### Custom Signals

Many of the components built into ProtoTwin provide their own set of signals. However, it is also possible to create your own components with their own set of signals. This is done my creating a scripted component inside of ProtoTwin and assigning that component to one or more entities. The example below demonstrates a simple custom component that generates a sinusoidal wave and provides a readable signal for the amplitude of the wave. The value of this signal can be read at runtime through the ProtoTwin Connect python client.

```
import { Component, type Entity, IO, DoubleSignal, Access } from "prototwin";

export class SineWaveGeneratorIO extends IO {
    public wave: DoubleSignal;

    public constructor(component: SineWaveGenerator) {
        super(component);
        this.wave = new DoubleSignal(0, Access.Readable);
        this.assign(); // Assign addresses to signals so that they can be accessed by connected clients (e.g. Python)
    }
}

export class SineWaveGenerator extends Component {
    #io: SineWaveGeneratorIO;
    
    public override get io(): SineWaveGeneratorIO {
        return this.#io;
    }

    constructor(entity: Entity) {
        super(entity);
        this.#io = new SineWaveGeneratorIO(this);
    }

    public override update(dt: number) {
        this.#io.wave.value = Math.sin(this.entity.world.time);
    }
}
```

## Example

This example demonstrates training an [inverted pendulum to swing up and balance](https://www.youtube.com/watch?v=W9wx2ZqYVJA).
Note that this example requires [ProtoTwin Connect](https://prototwin.com) to be installed on your local machine.

```
# STEP 1: Import dependencies
import prototwin_gymnasium
import prototwin
import asyncio
import os
import math
import time
import keyboard
import numpy as np
import torch as th
from typing import Tuple
from gymnasium import spaces
from stable_baselines3 import PPO
from stable_baselines3.common.policies import BasePolicy
from stable_baselines3.common.callbacks import EvalCallback

# STEP 2: Define signal addresses (obtain these values from ProtoTwin)
address_time = 0
address_cart_target_velocity = 3
address_cart_position = 5
address_cart_velocity = 6
address_cart_force = 7
address_pole_angle = 12
address_pole_angular_velocity = 13

# STEP 3: Create your environment by extending the base environment
class CartPoleEnv(prototwin_gymnasium.Env):
    def __init__(self, client: prototwin.Client) -> None:
        super().__init__(client)
        self.x_threshold = 0.65 # Maximum cart distance

        # The action space contains only the cart's target velocity
        action_high = np.array([1.0], dtype=np.float32)
        self.action_space = spaces.Box(-action_high, action_high, dtype=np.float32)

        # The observation space contains:
        # 0. A measure of the cart's distance from the center, where 0 is at the center and +/-1 is at the limit.
        # 1. A measure of the angular distance of the pole from the upright position, where 0 is at the upright position and 1 is at the down position.
        # 2. The cart's current velocity (m/s).
        # 3. The pole's angular velocity (rad/s).
        observation_high = np.array([1, 1, np.finfo(np.float32).max, np.finfo(np.float32).max], dtype=np.float32)
        self.observation_space = spaces.Box(-observation_high, observation_high, dtype=np.float32)

    def reward(self, obs):
        distance = 1 - math.fabs(obs[0]) # How close the cart is to the center
        angle = 1 - math.fabs(obs[1]) # How close the pole is to the upright position
        force = math.fabs(self.get(address_cart_force)) # How much force is being applied to drive the cart's motor
        return (angle * angle) * 0.8 + (distance * distance) * 0.2 - force * 0.001

    def reset(self, seed = None):
        super().reset(seed=seed)
        return np.array([0, 0])

    def step(self, action):
        self.set(address_cart_target_velocity, action) # Apply action by setting the cart's target velocity
        super().step() # Step the simulation forwards by one time-step
        time = self.get(address_time) # Read the current simulation time
        cart_position = self.get(address_cart_position) # Read the current cart position
        cart_velocity = self.get(address_cart_velocity) # Read the current cart velocity
        pole_angle = self.get(address_pole_angle) # Read the current pole angle
        pole_angular_velocity = self.get(address_pole_angular_velocity) # Read the current pole angular velocity
        pole_angular_distance = math.atan2(math.sin(math.pi - pole_angle), math.cos(math.pi - pole_angle)) # Calculate angular distance from upright position
        obs = np.array([cart_position / self.x_threshold, pole_angular_distance / math.pi, cart_velocity, pole_angular_velocity]) # Set observation space
        reward = self.reward(obs) # Calculate reward
        done = abs(obs[0]) > 1 # Terminate if cart goes beyond limits
        truncated = time > 20 # Truncate after 20 seconds
        return obs, reward, done, truncated, {}

# STEP 4: Setup the training session
async def train():
    # Start ProtoTwin Connect
    client = await prototwin.start()

    # Load the ProtoTwin model
    filepath = os.path.join(os.path.dirname(__file__), "CartPole.ptm")
    await client.load(filepath)

    # Create the environment
    env = CartPoleEnv(client)

    # Define the ML model
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./tensorboard/")

    # Create evaluation callback to regularly save the best trained model
    eval_callback = EvalCallback(env, 
                                 best_model_save_path='./logs/best_model',
                                 log_path='./logs/results', eval_freq=10000,
                                 deterministic=True, render=False)

    # Start learning!
    model.learn(total_timesteps=2_000_000, callback=eval_callback)

# STEP 5: Setup the evaluation session
async def evaluate():
    # Start ProtoTwin Connect
    client = await prototwin.start()

    # Load the ProtoTwin model
    filepath = os.path.join(os.path.dirname(__file__), "CartPole.ptm")
    await client.load(filepath)
    
    # Create the environment
    env = CartPoleEnv(client)

    # Load the trained ML model
    model = PPO.load("logs/best_model/best_model", env)

    # Run simulation at real-time speed
    while True:
        env.reset()
        done = False
        obs = [0, 0, 0, 0]
        start_wall_time = time.perf_counter()
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, truncated, info = env.step(action)
            if keyboard.is_pressed("r"):
                break
            current_wall_time = time.perf_counter()
            elapsed_wall_time = current_wall_time - start_wall_time
            elapsed_sim_time = client.get(address_time)
            sleep_time = elapsed_sim_time - elapsed_wall_time
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)

asyncio.run(train())
```

## Exporting to ONNX

It is possible to export trained models to the ONNX format. This can be used to embed trained agents into ProtoTwin models for inferencing. Please refer to the [Stable Baselines exporting documentation](https://stable-baselines3.readthedocs.io/en/master/guide/export.html) for further details. The example provided below shows how to export the trained Cart Pole model to ONNX.

```
# Export to ONNX for embedding into ProtoTwin models using ONNX Runtime Web
def export():
    class OnnxableSB3Policy(th.nn.Module):
        def __init__(self, policy: BasePolicy):
            super().__init__()
            self.policy = policy

        def forward(self, observation: th.Tensor) -> Tuple[th.Tensor, th.Tensor, th.Tensor]:
            return self.policy(observation, deterministic=True)
    
    # Load the trained ML model
    model = PPO.load("logs/best_model/best_model", device="cpu")

    # Create the Onnx policy
    onnx_policy = OnnxableSB3Policy(model.policy)

    observation_size = model.observation_space.shape
    dummy_input = th.randn(1, *observation_size)
    th.onnx.export(onnx_policy, dummy_input, "CartPole.onnx", opset_version=17, input_names=["input"], output_names=["output"])
```

## Inference in ProtoTwin

It is possible to embed trained agents into ProtoTwin models. To do this, you must create a scripted component that loads the ONNX model, feeds observations into the model and finally applies the output actions. Note that this example assumes that the ONNX file has been included into the model by dragging the file into the script editor's file explorer. Alternatively, the ONNX file can be loaded from a URL.

```
import { Component, type Entity, File, Handle, MotorComponent, Util } from "prototwin";
import * as ort from "https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/esm/ort.min.js";

export class CartPole extends Component {
    #session: any;
    #observationData: Float32Array;
    #observationDimensions: number[];

    public cartMotor: Handle<MotorComponent>;
    public poleMotor: Handle<MotorComponent>;

    constructor(entity: Entity) {
        super(entity);
        this.#observationData = new Float32Array(4);
        this.#observationDimensions = [1, 4];
        this.cartMotor = this.handle(MotorComponent);
        this.poleMotor = this.handle(MotorComponent);
    }

    public override async initializeAsync() {
        ort.env.wasm.wasmPaths = "https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/";
        const model = File.read("/model/scripts/CartPole.onnx");
        this.#session = await ort.InferenceSession.create(model);
    }

    public override async updateAsync(dt: number) {
        const cartMotor = this.cartMotor.value;
        const poleMotor = this.poleMotor.value;
        if (this.#session !== null && cartMotor !== null && poleMotor !== null) {
            // Get observations
            const cartPosition = cartMotor.currentPosition;
            const cartVelocity = cartMotor.currentVelocity;
            const poleAngularDistance = Util.signedAngularDifference(poleMotor.currentPosition, Math.PI);
            const poleAngularVelocity = poleMotor.currentVelocity;
            
            // Create observation tensor
            const data = this.#observationData;
            data[0] = cartPosition / 0.65;
            data[1] = poleAngularDistance / Math.PI;
            data[2] = cartVelocity;
            data[3] = poleAngularVelocity;
            const observations = new ort.Tensor("float32", data, this.#observationDimensions);

            // Run inference
            const results = await this.#session.run({ "input": observations });

            // Apply actions
            cartMotor.targetVelocity = Util.clamp(results.output.data[0], -1, 1);
        }
    }
}
```