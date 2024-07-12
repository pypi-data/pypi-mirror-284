from setuptools import setup, find_packages

setup(
    name='my_sample_package',  # Ensure this name is unique on PyPI
    version='0.1',
    packages=find_packages(),
    description='A simple package to add two numbers',
    author='periyanayagam',
    author_email='periyanayagam.anthonysamy@itbeezone.in',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
