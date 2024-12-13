from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

world_file_path = os.path.join(
    get_package_share_directory('RyanAdolfsOutdoor'), 'worlds', 'OutdoorSimulation.wbt'
)

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=world_file_path,
            description='Path to the Webots world file'
        ),
        Node(
            package='webots_ros2',
            executable='webots_launcher',
            name='webots',
            output='screen',
            arguments=['--world', LaunchConfiguration('world')]
        )
    ])