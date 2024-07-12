from setuptools import setup

setup(
    name="pytest_documentary",
    version="0.1.0",
    description="A simple pytest plugin to generate test documentation",
    packages=["pytest_documentary"],
    entry_points={
        "pytest11": [
            "pytest_documentary = pytest_documentary.plugin"
        ],
    },
    install_requires=[
        "pytest",
        "pandas",
        "openpyxl",
    ],
    classifiers=["Framework :: Pytest"],
)