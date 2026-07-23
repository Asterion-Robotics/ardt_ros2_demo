#ifndef ARDT_ROS2_DEMO_PKG_2__COUNTER_HPP_
#define ARDT_ROS2_DEMO_PKG_2__COUNTER_HPP_

#include <cstdint>

namespace ardt_ros2_demo_pkg_2
{

/// \brief A bounded counter — the C++ API-doc showcase of the ardt demo.
///
/// Mirrors the Python `counting` module of `ardt_ros2_demo_pkg_1`: the value
/// advances toward a target one clamped step at a time and never overshoots.
class Counter
{
public:
  /// \brief Create a counter starting at `initial`.
  explicit Counter(std::int64_t initial = 0);

  /// \brief Advance one step toward `target`, clamping at it.
  /// \param target The value to move toward (may be below the current value).
  /// \param step Positive step size.
  /// \return The value after the step.
  /// \throws std::invalid_argument If `step` is not positive.
  std::int64_t advance_toward(std::int64_t target, std::int64_t step = 1);

  /// \brief The current value.
  std::int64_t value() const;

  /// \brief True when the counter sits exactly on `target`.
  bool is_done(std::int64_t target) const;

private:
  std::int64_t value_;
};

}  // namespace ardt_ros2_demo_pkg_2

#endif  // ARDT_ROS2_DEMO_PKG_2__COUNTER_HPP_
