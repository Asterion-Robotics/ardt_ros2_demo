cmake_minimum_required(VERSION 3.16)
project(ardt_demo_ros2_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(action_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CounterLimits.msg"
  "msg/DemoStatus.msg"
  "msg/StepEvent.msg"
  "srv/GetHistory.srv"
  "srv/Reset.srv"
  "srv/SetCounter.srv"
  "action/CountTo.action"
  "action/Oscillate.action"
  DEPENDENCIES builtin_interfaces action_msgs
)

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  ament_add_pytest_test(interfaces_smoke test)
endif()

ament_package()
