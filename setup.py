import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["pandas>=0.24.1", "requests>=2.21.0"]

setuptools.setup(
    name="batdata",
    version="0.1.0",
    author="Bien An Toan",
    author_email="batdata@bienantoam.com.vn",
    description="A package to download Vietnam stock market data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = install_requires
)
