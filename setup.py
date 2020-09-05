from setuptools import find_packages, setup

setup(
    name="aoji",
    version="1.0.0",
    description="Aoji supports createing your local git project for kaggle.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    author="Nayu.T.S",
    url="https://github.com/tasotasoso/aoji",
    keywords="kaggle python git",
    packages=find_packages(),
    install_requires=[
        "kaggle",
        "pathlib",
        "GitPython"
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: Apache-2.0",
    ],
)