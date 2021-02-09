import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pyconfig_gen",
    version = "1.2.0",
    author = "sakaki",
    maintainer = "GenPi64 Team",
    description = "GUI editor for /boot/config.txt on RPi3 SBCs",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/genpi64/pyconfig_gen",
    packages = setuptools.find_packages(),
    scripts = ["bin/pyconfig_gen"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
    ],
)
