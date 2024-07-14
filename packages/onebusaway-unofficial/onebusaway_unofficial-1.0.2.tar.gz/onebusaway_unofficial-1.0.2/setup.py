# setup.py
from setuptools import setup

setup(
    name="onebusaway-unofficial",
    version="1.0.2",
    description="The OneBusAway Python Client (unofficial) is a Python library for interacting with the OneBusAway API. It provides a simple and convenient way to access real-time transit data, schedules, and other information from various transit agencies.",
    author="Chaitanya Sharma",
    url="https://github.com/CheeksTheGeek/onebusaway-python",
    license="MIT",
    packages=["onebusaway"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
