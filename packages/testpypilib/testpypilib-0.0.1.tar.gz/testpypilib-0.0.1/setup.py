"""
use `MANIFEST.in` file to add arbitrary files to package
"""


from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="testpypilib",
    version="0.0.1",
    description="small description",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://wooordhunt.ru/",
    author="Author Name",
    author_email="AuthorName@emai.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy"],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "testpypilib-hello = testpypilib:function_uses_numpy",
        ],
    },
)
