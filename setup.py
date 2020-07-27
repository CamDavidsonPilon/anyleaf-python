import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anyleaf",
    version="0.1.7.1",
    author="Anyleaf",
    author_email="anyleaf@anyleaf.org",
    description="Driver for the Anyleaf pH sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anyleaf/anyleaf_ph",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers ",
    ],
    python_requires=">=3.7",
    license="MIT",
    install_requires=[
        'adafruit-circuitpython-ads1x15>=2.2.1'
        'filterpy>=1.4.5',
        'numpy>=1.18.4',
    ]
)
