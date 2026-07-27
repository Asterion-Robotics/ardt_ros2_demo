Interfaces
==========

The public ROS 2 interface of the demo stack, defined by the
``ardt_demo_ros2_msgs`` package. All interaction with the demo counter —
topics, services and actions — goes through the definitions below; interfaces
not listed here are internal and may change without notice.

This reference is generated from the interface definitions at every
documentation build and always matches the sources of this version.

.. note::

   ``demo_counter`` implements the ``DemoStatus`` topic and the ``SetCounter``
   service; the remaining definitions exist so this page exercises every shape
   the ``ros2-interfaces`` directive renders — defaults, constants, arrays of
   package-local messages, and an empty request.

.. toctree::
   :maxdepth: 2

   messages
   services
   actions
