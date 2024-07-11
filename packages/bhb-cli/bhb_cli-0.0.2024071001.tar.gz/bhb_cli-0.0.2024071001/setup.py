from setuptools import setup, find_packages

VERSION = '0.0.2024071001'
DESCRIPTION = 'bhb-cli'

# Setting up
setup(
    name="bhb-cli",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
