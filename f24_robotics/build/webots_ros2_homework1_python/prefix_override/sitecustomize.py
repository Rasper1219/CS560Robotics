import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ryan/Desktop/f24_robotics/install/webots_ros2_homework1_python'
