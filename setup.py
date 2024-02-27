from setuptools import setup, find_packages

setup(
    name="q2-cross-study-ml",
    version=version,
    packages=find_packages(),
    # pandas, q2templates and q2-dummy-types are only required for the dummy
    # methods and visualizers provided as examples. Remove these dependencies
    # when you're ready to develop your plugin, and add your own dependencies
    # (if there are any).
    install_requires=['pandas'],
    author="Petri Vänni",
    author_email="petri.vanni@oulu.fi",
    description="Tool for cross-study machine learning analyses",
    entry_points={
        "qiime2.plugins":
        ["q2-cross-study-ml=q2-cross-study-ml.plugin_setup:plugin"]
    },
)