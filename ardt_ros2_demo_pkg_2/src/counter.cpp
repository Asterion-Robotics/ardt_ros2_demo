#include "ardt_ros2_demo_pkg_2/counter.hpp"

#include <algorithm>
#include <stdexcept>

namespace ardt_ros2_demo_pkg_2
{

Counter::Counter(std::int64_t initial)
: value_(initial)
{
}

std::int64_t Counter::advance_toward(std::int64_t target, std::int64_t step)
{
  if (step <= 0) {
    throw std::invalid_argument("step must be positive");
  }
  if (value_ < target) {
    value_ = std::min(value_ + step, target);
  } else if (value_ > target) {
    value_ = std::max(value_ - step, target);
  }
  return value_;
}

std::int64_t Counter::value() const
{
  return value_;
}

bool Counter::is_done(std::int64_t target) const
{
  return value_ == target;
}

}  // namespace ardt_ros2_demo_pkg_2
