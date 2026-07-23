"""The demo counter node.

Publishes :class:`~ardt_demo_ros2_msgs.msg.DemoStatus` on ``~/status`` once a
second and serves ``~/set`` (:class:`~ardt_demo_ros2_msgs.srv.SetCounter`).
All counting behavior lives in :mod:`.counting`.
"""

from __future__ import annotations

import rclpy
from rclpy.node import Node

from ardt_demo_ros2_msgs.msg import DemoStatus
from ardt_demo_ros2_msgs.srv import SetCounter

from .counting import advance, is_done


class DemoCounter(Node):
    """Counts toward a target and reports its state.

    Parameters are deliberately absent: the node exists to give the ardt demo
    a runnable, testable surface, not to be useful.
    """

    def __init__(self) -> None:
        super().__init__("demo_counter")
        self._count = 0
        self._target = 0
        self._publisher = self.create_publisher(DemoStatus, "~/status", 10)
        self._service = self.create_service(SetCounter, "~/set", self._on_set)
        self._timer = self.create_timer(1.0, self._on_tick)

    def _on_tick(self) -> None:
        """Advance one step and publish the current state."""
        self._count = advance(self._count, self._target)
        message = DemoStatus()
        message.stamp = self.get_clock().now().to_msg()
        message.count = self._count
        message.state = (
            DemoStatus.STATE_IDLE if is_done(self._count, self._target) else DemoStatus.STATE_COUNTING
        )
        self._publisher.publish(message)

    def _on_set(self, request: SetCounter.Request, response: SetCounter.Response) -> SetCounter.Response:
        """Jump the target; the counter walks there one tick at a time."""
        response.previous = self._target
        response.success = True
        self._target = request.target
        return response


def main(argv: list[str] | None = None) -> None:
    """Entry point of the ``demo_counter`` executable."""
    rclpy.init(args=argv)
    node = DemoCounter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
