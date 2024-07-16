
from setuptools import setup, find_packages

setup(
    name='samruddhk',
    version='1.1.0',  # Update version number
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    python_requires='>=3.6',
    author='SAMRUDDH K',
    author_email='samruddh.k52@gmail.com',
    description='A collection of algorithms including BFS, DFS, Dijkstra\'s, etc.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SAMRUDDH15/samruddhk.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
)
