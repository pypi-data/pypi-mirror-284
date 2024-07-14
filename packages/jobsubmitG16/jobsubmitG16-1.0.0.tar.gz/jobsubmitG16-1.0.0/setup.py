from setuptools import find_packages, setup
import io 
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='jobsubmitG16',
    packages=find_packages(),
    version='1.0.0',
    author="Mohammed A. Jabed,",
    author_email="jabed.abu@gmail.com",
    keywords=['gaussian', 'compchem', 'ccast','ndsu'],
    install_requires=['argparse'], 
    python_requires='>=3.0',
    description='A python program for bulk job submission in NDSU CCAST Prime HPC cluster',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'jobsubmitG16 = jobsubmitG16.jobsubmitG16:main',
        ],
    }
)
