from setuptools import setup, find_packages

setup(
    name="IPSpin",
    version="0.1.0",
    description="A Python library for interacting with IPSpin Services.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="IPSpin",
    author_email="olealgoritme@gmail.com",
    url="https://github.com/olealgoritme/IPSpin_python",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
