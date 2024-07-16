import sys

from setuptools import setup
from wheel.bdist_wheel import bdist_wheel


class no_wheel(bdist_wheel):
    def run(self):
        sys.exit(
            "This package is currently under development at "
            "https://github.com/lab-cosmo and will be published on "
            "PyPI when a first version is ready."
        )


if __name__ == "__main__":
    setup(
        cmdclass={"bdist_wheel": no_wheel},
    )
