from setuptools import setup, find_packages

setup(
    name="windows-network-optimizer",
    version="1.0.0",
    description="A Python CLI tool to optimize Windows network settings for lower latency and better throughput.",
    author="adityaoryza",
    packages=find_packages(),
    py_modules=["main"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "network-optimizer=main:main",
        ],
    },
)
