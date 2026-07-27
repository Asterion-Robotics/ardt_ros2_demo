# ardt_ros2_demo

[![ci](https://github.com/Asterion-Robotics/ardt_ros2_demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Asterion-Robotics/ardt_ros2_demo/actions/workflows/ci.yml)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://asterion-robotics.github.io/ardt_ros2_demo/)
[![license](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)

The demo repository for the [ardt](https://github.com/Asterion-Robotics/ardt) CI tools: a minimal but complete ROS 2 workspace exercising the build, test and doc tasks (and, via `ros-ci` and `docs-ci`, the pipeline plane).

## Layout

| Package | Type | What it demonstrates |
|---|---|---|
| [`ardt_ros2_demo`](ardt_ros2_demo/) | aggregator | groups the others; hosts the repo docs ([doc/](ardt_ros2_demo/doc/)) |
| [`ardt_ros2_demo_pkg_1`](ardt_ros2_demo_pkg_1/) | `ament_python` | a counter node; pure logic split out for tests + autodoc |
| [`ardt_ros2_demo_pkg_2`](ardt_ros2_demo_pkg_2/) | `ament_cmake` | a C++ library with Doxygen comments + gtest |
| [`ardt_demo_ros2_msgs`](ardt_demo_ros2_msgs/) | interfaces | msg/srv/action with the comment conventions the doc tooling renders |

## Commands

Install ardt once as a uv tool (see [ardt's README](https://github.com/Asterion-Robotics/ardt#installation) for the full command), then, from a checkout of this repo:

```bash
ardt deps        # rosdep install
ardt build       # colcon build
ardt test        # colcon test + summary (smoke tests in every package)
ardt doc build   # doxygen + sphinx -> build/doc/html/index.html
```

The docs show all four doc features: hand-written RST (with math and a mermaid diagram), Python API via autodoc (no colcon build needed — ROS imports are mocked), C++ API via Doxygen/breathe, and the interface tables rendered straight from the `.msg`/`.srv`/`.action` files by the ardt `ros2-interfaces` directive. Repo-side doc footprint: one 5-line `conf.py` plus content — theme, extensions and Doxyfile are ardt-owned.

## The pipeline plane

Nothing above needs Docker. The two pipelines do, and they run the exact same tasks inside containers:

```bash
ardt pipe run ros-ci    # deps/build/test as image stages; a red test fails the image build
ardt pipe run docs-ci   # the versioned site (working tree + every v* tag) -> public/
```

[`.github/workflows/ci.yml`](.github/workflows/ci.yml) is the whole CI: install ardt, call those two commands, publish `public/` to GitHub Pages on tags. The repo contains no Dockerfile and no colcon invocation — the recipes are ardt's, pinned by `ardt.version` in [`ardt.yaml`](ardt.yaml).

## License

Apache-2.0 — see [LICENSE](LICENSE).
