import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NumpyLayer",
    version="0.1a",
    author="Siu",
    author_email="siukkokko@gmail.com",
    description="Npai is deeplearning package",
    long_description=long_description,
    url="https://github.com/Kbrain2/Npai.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)