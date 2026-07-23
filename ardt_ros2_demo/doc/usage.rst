Usage
=====

Everything goes through ``ardt``, from a checkout of this repo:

.. code-block:: bash

   ardt deps        # rosdep install
   ardt build       # colcon build
   ardt test        # colcon test + summary
   ardt doc build   # doxygen + sphinx -> build/doc/html

Run the demo node after a build:

.. code-block:: bash

   . install/setup.bash
   ros2 run ardt_ros2_demo_pkg_1 demo_counter
   ros2 service call /demo_counter/set ardt_demo_ros2_msgs/srv/SetCounter "{target: 5}"

How the counter walks
---------------------

Each tick moves the value one clamped step toward the target
(:func:`ardt_ros2_demo_pkg_1.counting.advance`); after :math:`n` ticks the
value is

.. math::

   c_n = c_0 + \operatorname{sgn}(t - c_0)\,\min(n\,s,\ |t - c_0|)

which reaches the target :math:`t` in :math:`\lceil |t - c_0| / s \rceil`
ticks of step size :math:`s`.
