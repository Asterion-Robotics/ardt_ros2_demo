"""Smoke: the generated interfaces import and expose their declared surface.

Runs under `colcon test` (the package must be built and sourced).
"""


def test_msg_constants() -> None:
    from ardt_demo_ros2_msgs.msg import DemoStatus

    assert DemoStatus.STATE_IDLE == 0
    assert DemoStatus.STATE_COUNTING == 1
    assert DemoStatus().state == DemoStatus.STATE_IDLE


def test_srv_roundtrip_defaults() -> None:
    from ardt_demo_ros2_msgs.srv import SetCounter

    assert SetCounter.Request().target == 0
    assert SetCounter.Response().success is False


def test_action_sections_exist() -> None:
    from ardt_demo_ros2_msgs.action import CountTo

    assert CountTo.Goal().target == 0
    assert CountTo.Result().final_count == 0
    assert CountTo.Feedback().current == 0


def test_msg_field_defaults() -> None:
    from ardt_demo_ros2_msgs.msg import CounterLimits, StepEvent

    limits = CounterLimits()
    assert limits.min_value == -100
    assert limits.max_value == 100
    assert limits.wrap is False
    assert StepEvent.REASON_ACTION == 2


def test_nested_and_empty_interfaces() -> None:
    from ardt_demo_ros2_msgs.msg import StepEvent
    from ardt_demo_ros2_msgs.srv import GetHistory, Reset

    assert Reset.Request() is not None  # deliberately empty request
    history = GetHistory.Response()
    history.steps = [StepEvent()]  # array of a package-local message
    assert len(history.steps) == 1


def test_oscillate_defaults() -> None:
    from ardt_demo_ros2_msgs.action import Oscillate

    assert Oscillate.Goal().cycles == 1
    assert Oscillate.Result().interrupted is False
    assert Oscillate.Feedback().cycle == 0
