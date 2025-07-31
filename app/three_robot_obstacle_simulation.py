import irsim

env = irsim.make('three_robot_multiple_goals_one_obstacle.yaml') # initialize the environment with multiple robots and obstacle

print(f"Simulation started with {len(env.robot_list)} robots and {len(env.obstacle_list)} obstacle(s)")
print("Obstacle positioned at the center of the map with radius 1.5")
print("\nRobot starting positions:")
for i, robot in enumerate(env.robot_list, 1):
    print(f"Robot {i}: Starting at ({robot.state[0]}, {robot.state[1]})")

print("\nGoals have been adjusted to avoid the central obstacle")

for step in range(1500): # run the simulation for 1500 steps to allow time for navigation around obstacle

    env.step()  # update the environment
    env.render() # render the environment

    # Print progress every 150 steps
    if step % 150 == 0:
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
