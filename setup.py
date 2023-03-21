from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='bettydash',
    url='https://github.com/onesixx/bettydash',
    version='0.2',
    author='onesixx',
    author_email='onesixx@nate.com',
    description='A Python package for dashboard',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.19.2',
        'pandas>=1.1.2',
        'matplotlib>=3.3.2',
    ],
)
