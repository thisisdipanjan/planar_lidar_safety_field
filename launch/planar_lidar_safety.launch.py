from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='planar_lidar_safety_field',
            executable='planar_lidar_safety_node',
            name='planar_lidar_safety',
            parameters=['config/planar_lidar_safety_params.yaml']
        )
    ])