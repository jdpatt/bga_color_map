from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="part_map",
    version="2.1.0",
    description="Part Visualizer",
    long_description=readme(),
    url="https://github.com/jdpatt/part_map",
    author="David Patterson",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(include=["part_map", "part_map.*"]),
    include_package_data=True,
    install_requires=["openpyxl", "Click", "natsort", "PySide2"],
    entry_points={"console_scripts": ["part-map = part_map.cli:cli"]},
    zip_safe=False,
)
