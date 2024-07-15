from setuptools import setup, find_packages


setup(
    name="prettypi",
    version="0.1.3",

    description="A Python library for pretty printing and enhanced console output.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author="Vodkas",
    author_email="vodkas3630@gmail.com",
    url="https://github.com/Glawnn/PrettyPi",
    project_urls={
        "Documentation": "https://github.com/Glawnn/PrettyPi",
        "Source": "https://github.com/Glawnn/PrettyPi",
    },
    license="MIT",
    packages=find_packages(exclude=("tests")),
    install_requires=[
        "setuptools",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.8",
)
