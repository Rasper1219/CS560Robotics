# CS460-Proj3Part3

## Project Description: 

20%-Generalized autonomous search (15% for graduate students)
1. Expand your team's autonomous controller to look for a single april tag
2. Put controller in a ROS 2 package that can be executed using a launch command.
3. Document the executing of the controller in a README.md
4. Choose two of the attached simulated indoor environments, randomly place a tag on a wall or furntiture
5. Run 3 trials of 10 minutes in each of two environments with tags placed in different places and with random start points (use a random generator to determine location/start)
6. Analyize the performance of your controller by calculating coverage as a function of time and recording the time to find a randomly placed tag
7. a) Turn in the github link to the ROS 2 paackage for your controller in the assignment notes. b) Turn in the performance tables/graphs and analysis as a pdf submitted to blackbaord link




## Prerequisites

Ensure you have ROS2 installed and sourced (tested with ROS2 Humble). You will also need Webots and `webots_ros2` installed.

1. Install Webots if you haven't already:
    ```bash
    sudo apt update
    sudo apt install webots
    ```

2. Install the `webots_ros2` package:
    ```bash
    sudo apt install ros-humble-webots-ros2
    ```

## Installation

1. Clone the repository:
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/ggkarabas/CS460-Proj3Part3.git
    ```

2. Build the package:
    ```bash
    cd ~/ros2_ws
    colcon build
    ```

3. Source the workspace:
    ```bash
    source install/setup.bash
    ```

## Running the Simulation

To run the simulation, use the following command:

```bash
ros2 launch webots_ros2_homework1_python f23_robotics_1_launch.py world:=maze1_smallest.wbt
```
