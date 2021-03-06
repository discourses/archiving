import setuptools


NAME = 'archiving'
VERSION = '0.0.1'
DESCRIPTION = 'A simple tool for archiving data files'
AUTHOR = 'greyhypotheses'
URL = 'https://github.com/discourses/archiving'
PYTHON_REQUIRES = '=3.7.7'


with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()


setuptools.setup()(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme_text,
    author=AUTHOR,
    url=URL,
    python_requires=PYTHON_REQUIRES,
    license=license_text,
    packages=setuptools.find_packages(exclude=['docs', 'tests'])
)
