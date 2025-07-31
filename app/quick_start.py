import irsim

env = irsim.make('robot_world.yaml') # initialize the environment with the configuration file

for i in range(800): # run the simulation for 800 steps to allow time for multiple goals

    env.step()  # update the environment
    env.render() # render the environment

    # Print current goal progress
    if i % 50 == 0:  # Print every 50 steps
        current_goal = env.robot.goal
        if current_goal is not None:
            print(f"Step {i}: Current goal: ({current_goal[0]}, {current_goal[1]})")
        else:
            print(f"Step {i}: All goals completed!")

    if env.done(): 
        print("All goals reached! Simulation complete.")
        break
        
env.end() # close the environment
