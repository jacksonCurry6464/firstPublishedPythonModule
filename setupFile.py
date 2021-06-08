from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.01'
DESCRIPTION = 'Alamo Algorithm Class Implementation'
LONG_DESCRIPTION = 'Python package that allows the user to use the alamo algorithm for interpolation'

# Setting up
setup(
    name="alamoAlg",
    version=VERSION,
    author="Jackson Curry",
    author_email="<jackson.curry6464@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'Alamo', 'Interpolation'],
    classifiers=[
        "Development Status :: Testing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)