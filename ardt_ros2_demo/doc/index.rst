ardt_ros2_demo
==============

The demo repository for the `ardt <https://github.com/Asterion-Robotics/ardt>`_
tooling: four small ROS 2 packages exercising the build, test and doc tasks.

.. mermaid::

   graph LR
      msgs[ardt_demo_ros2_msgs] --> py[ardt_ros2_demo_pkg_1 <br/> Python node]
      msgs -.-> cpp[ardt_ros2_demo_pkg_2 <br/> C++ library]
      py --> meta[ardt_ros2_demo <br/> metapackage + docs]
      cpp --> meta

.. toctree::
   :maxdepth: 2

   usage
   interfaces/index
   api/python
   api/cpp
