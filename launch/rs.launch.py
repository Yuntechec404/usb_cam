# usb_cam_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            namespace='usb_cam_0',  # 設置 namespace
            parameters=[
                '/home/user/ros2_ws/src/usb_cam/config/params_1.yaml'  # 加載參數文件
            ],
            remappings=[
                # 您可以在此處加入其他需要的 topic remap
            ]
        )
    ])
