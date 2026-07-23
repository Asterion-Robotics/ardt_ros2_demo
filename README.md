# ardt_ros2_demo

The demo repository for the [ardt](https://github.com/Asterion-Robotics/ardt)
CI tools: a minimal but complete ROS 2 workspace exercising the build, test
and doc tasks (and, via `ros-ci`, the pipeline plane).

## Layout

| Package | Type | What it demonstrates |
|---|---|---|
| [`ardt_ros2_demo`](ardt_ros2_demo/) | metapackage | groups the others; hosts the repo docs ([doc/](ardt_ros2_demo/doc/)) |
| [`ardt_ros2_demo_pkg_1`](ardt_ros2_demo_pkg_1/) | `ament_python` | a counter node; pure logic split out for tests + autodoc |
| [`ardt_ros2_demo_pkg_2`](ardt_ros2_demo_pkg_2/) | `ament_cmake` | a C++ library with Doxygen comments + gtest |
| [`ardt_demo_ros2_msgs`](ardt_demo_ros2_msgs/) | interfaces | msg/srv/action with the comment conventions the doc tooling renders |

## Commands

```bash
ardt deps        # rosdep install
ardt build       # colcon build
ardt test        # colcon test + summary (smoke tests in every package)
ardt doc build   # doxygen + sphinx -> build/doc/html/index.html
```

The docs show all four doc features: hand-written RST (with math and a
mermaid diagram), Python API via autodoc (no colcon build needed — ROS
imports are mocked), C++ API via Doxygen/breathe, and the interface tables
rendered straight from the `.msg`/`.srv`/`.action` files by the ardt
`ros2-interfaces` directive. Repo-side doc footprint: one 5-line `conf.py`
plus content — theme, extensions and Doxyfile are ardt-owned.
