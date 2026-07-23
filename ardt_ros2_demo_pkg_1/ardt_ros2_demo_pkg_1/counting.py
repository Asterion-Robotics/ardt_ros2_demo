"""Pure counting logic — importable without ROS.

The node in :mod:`.demo_node` is a thin shell over these functions, so the
interesting behavior stays unit-testable anywhere (and documentable by
autodoc without a colcon build).
"""

from __future__ import annotations


def advance(current: int, target: int, step: int = 1) -> int:
    """One counting step from ``current`` toward ``target``, clamped at it.

    Args:
        current: The value before the step.
        target: The value being counted toward (may be below ``current``).
        step: Positive step size.

    Returns:
        The value after the step; never overshoots ``target``.

    Raises:
        ValueError: If ``step`` is not positive.
    """
    if step <= 0:
        raise ValueError(f"step must be positive, got {step}")
    if current < target:
        return min(current + step, target)
    if current > target:
        return max(current - step, target)
    return current


def is_done(current: int, target: int) -> bool:
    """True when the counter has reached its target."""
    return current == target
