import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "code_parser",
    version="0.0.1",
    author="Viatcheslav ilearnToday",
    author_email="goodeitime@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilearnToday/FirstOtusHomework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",
    ],
)