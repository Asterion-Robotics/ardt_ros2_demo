from setuptools import find_packages, setup

package_name = "ardt_ros2_demo_pkg_1"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Asterion Robotics",
    maintainer_email="dev@asterion-robotics.com",
    description="Python demo package: a counter node over the demo interfaces",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "demo_counter = ardt_ros2_demo_pkg_1.demo_node:main",
        ],
    },
)
