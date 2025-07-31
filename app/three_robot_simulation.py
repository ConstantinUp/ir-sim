import irsim

env = irsim.make('three_robot_multiple_goals.yaml') # initialize the environment with multiple robots

print(f"Simulation started with {len(env.robot_list)} robots")
for i, robot in enumerate(env.robot_list, 1):
    print(f"Robot {i}: Starting at ({robot.state[0]}, {robot.state[1]})")

for step in range(1200): # run the simulation for 1200 steps to allow time for all robots to complete their goals

    env.step()  # update the environment
    env.render() # render the environment

    # Print progress every 100 steps
    if step % 100 == 0:
        print(f"\nStep {step}:")
        for i, robot in enumerate(env.robot_list, 1):
            current_goal = robot.goal
            if current_goal is not None:
                print(f"  Robot {i}: Moving to goal ({current_goal[0]}, {current_goal[1]})")
            else:
                print(f"  Robot {i}: All goals completed!")

    if env.done(): 
        print(f"\nAll robots completed their missions at step {step}!")
        break
        
env.end() # close the environment
