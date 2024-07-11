from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="skibidi",
    version="0.0.1",
    author="arpy8",
    description="skibidi", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    # entry_points={
    #     "console_scripts": [
    #         "rcps=rcps.main:main",
    #     ],
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages=find_packages(),
    # package_data={'rcps': ['*.txt', '*.json']},
)