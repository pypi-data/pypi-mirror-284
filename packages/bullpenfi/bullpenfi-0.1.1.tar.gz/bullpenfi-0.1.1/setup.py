from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bullpenfi",
    version="0.1.1",
    author="Hongjun Wu",
    author_email="hongjun@bullpen.fi",
    description="Bullpenfi's non-sensitive wrapper for many 3rd party APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bullpenfi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests", "numpy"],
)
