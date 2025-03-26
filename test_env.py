import gymnasium as gym
from environment.custom_env import MaternalHealthEnv

# Initialize the environment
env = MaternalHealthEnv()

# Reset the environment to get the initial state
state = env.reset()
done = False

print("Starting Environment Test...\n")

# Run a few steps to test the environment
for _ in range(10):
    action = env.action_space.sample()  # Random action selection
    state, reward, done, _ = env.step(action)  # Take a step
    env.render()  # Print state details

    if done:
        print("Episode finished!\n")
        break  # Exit loop if the episode ends

env.close()
print("Environment Test Completed!")
