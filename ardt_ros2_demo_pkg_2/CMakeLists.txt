cmake_minimum_required(VERSION 3.16)
project(ardt_ros2_demo_pkg_2)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
endif()

find_package(ament_cmake REQUIRED)

add_library(counter src/counter.cpp)
add_library(${PROJECT_NAME}::counter ALIAS counter)
target_include_directories(counter PUBLIC
  "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
  "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>")

install(DIRECTORY include/ DESTINATION include/${PROJECT_NAME})
install(TARGETS counter
  EXPORT export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)
ament_export_include_directories("include/${PROJECT_NAME}")

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  ament_add_gtest(test_counter test/test_counter.cpp)
  target_link_libraries(test_counter counter)
endif()

ament_package()
