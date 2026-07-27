// Copyright 2026 Asterion Robotics
// SPDX-License-Identifier: Apache-2.0

// Smoke: the counter advances, clamps and rejects bad steps.
#include <gtest/gtest.h>

#include <stdexcept>

#include "ardt_ros2_demo_pkg_2/counter.hpp"

using ardt_ros2_demo_pkg_2::Counter;

TEST(Counter, advances_toward_target_in_both_directions)
{
  Counter counter{0};
  EXPECT_EQ(counter.advance_toward(3), 1);
  Counter down{3};
  EXPECT_EQ(down.advance_toward(0), 2);
}

TEST(Counter, clamps_at_target)
{
  Counter counter{2};
  EXPECT_EQ(counter.advance_toward(3, 5), 3);
  EXPECT_TRUE(counter.is_done(3));
}

TEST(Counter, rejects_non_positive_steps)
{
  Counter counter{0};
  EXPECT_THROW(counter.advance_toward(3, 0), std::invalid_argument);
}
