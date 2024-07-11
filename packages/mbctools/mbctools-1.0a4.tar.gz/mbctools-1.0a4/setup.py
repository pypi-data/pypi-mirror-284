from setuptools import setup, find_packages

setup(
    name='mbctools',
    version='1.0a4',
    py_modules=['mbctools'],
    entry_points={
        'console_scripts': [
            'mbctools = mbctools:main',
        ],
    },
)