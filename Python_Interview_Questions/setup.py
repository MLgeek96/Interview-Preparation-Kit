from setuptools import setup 

with open("README.md", "r") as fp:
    long_description = fp.read()


setup(
    name="python_problem_sets",
    version="0.1.0",
    author="Jacson Chong",
    author_email="sagittarius.jacson@gmail.com",
    description="Problem Sets for practice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/MLgeek96/Interview-Preparation-Kit",
    install_requires=[
            'pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other / Proprietary License",
        "Operating System :: OS Independent"
    ]
)