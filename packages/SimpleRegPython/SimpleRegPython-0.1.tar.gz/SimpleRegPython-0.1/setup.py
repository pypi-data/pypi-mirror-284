from setuptools import setup, find_packages

setup(
    name='SimpleRegPython',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add any other dependencies here
    ],
    author='Arash Ardalan',
    author_email='a.ardalan07@gmail.com',
    description='A package for Pearson correlation and simple linear regression',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ArashArd/SimpleRegPython',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
