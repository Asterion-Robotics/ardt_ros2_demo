# Copyright 2026 Asterion Robotics
# SPDX-License-Identifier: Apache-2.0

"""Smoke: the pure counting logic — runs anywhere, no ROS needed."""

import pytest

from ardt_ros2_demo_pkg_1.counting import advance, is_done


def test_advance_moves_toward_target_in_both_directions() -> None:
    assert advance(0, 3) == 1
    assert advance(3, 0) == 2


def test_advance_clamps_at_target() -> None:
    assert advance(2, 3, step=5) == 3
    assert advance(3, 3) == 3


def test_step_must_be_positive() -> None:
    with pytest.raises(ValueError):
        advance(0, 3, step=0)


def test_is_done() -> None:
    assert is_done(3, 3)
    assert not is_done(2, 3)
