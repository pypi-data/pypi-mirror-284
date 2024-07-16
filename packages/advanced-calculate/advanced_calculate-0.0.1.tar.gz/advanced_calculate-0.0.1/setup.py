from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        f.read()


setup(
    name="advanced_calculate",
    version="0.0.1",
    author="kubatbaew",
    author_email="kubatbaew@gmail.com",
    description="Advanced calculator written in Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kubatbaew",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="calculate advanced"
)
