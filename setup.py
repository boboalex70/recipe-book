import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recipe-book",
    version="0.0.1",
    author="Alex Bochenek",
    description="A windows app to help make grocery lists.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boboalex70/recipe-book.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
