from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 第一個相機節點
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam_0',
            namespace='usb_cam_0',  # 設置第一個相機的 namespace
            parameters=[
                '/home/user/ros2_ws/src/usb_cam/config/params_1.yaml'  # 第一個相機的參數文件
            ],
            remappings=[
                # 需要的 topic remap 可以在這裡設置
            ]
        ),
        
        # 第二個相機節點
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam_1',
            namespace='usb_cam_1',  # 設置第二個相機的 namespace
            parameters=[
                '/home/user/ros2_ws/src/usb_cam/config/params_2.yaml'  # 第二個相機的參數文件
            ],
            remappings=[
                # 需要的 topic remap 可以在這裡設置
            ]
        )
    ])
