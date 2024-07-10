from setuptools import setup

PLUGIN_NAME = "polars"

microlib_name = f"flytekitplugins-{PLUGIN_NAME}"

plugin_requires = ["flytekit>=1.3.0b2,<2.0.0", "polars>=0.8.27,<0.17.0", "pandas"]

__version__ = "1.13.1a0"

setup(
    name=microlib_name,
    version=__version__,
    author="Robin Kahlow",
    description="Polars plugin for flytekit",
    namespace_packages=["flytekitplugins"],
    packages=[f"flytekitplugins.{PLUGIN_NAME}"],
    install_requires=plugin_requires,
    license="apache2",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"flytekit.plugins": [f"{PLUGIN_NAME}=flytekitplugins.{PLUGIN_NAME}"]},
)
