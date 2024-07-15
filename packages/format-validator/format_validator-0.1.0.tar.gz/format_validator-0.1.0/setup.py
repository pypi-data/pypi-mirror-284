from setuptools import setup, find_packages

setup(
    name='format_validator',
    version='0.1.0',
    description='A simple library to validate emails, phone numbers and dates in various formats',
    author='Ferenc Kovacs',
    author_email='kovacsferenc026@gmail.com',
    url='https://github.com/Ferref',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
