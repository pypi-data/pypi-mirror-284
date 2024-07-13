# setup.py
from setuptools import setup, find_packages

setup(
    name='my_unique_package_name',  # 更改为一个独特的包名
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_package = my_package:main',
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='A simple package to print COMS W3132 UNI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
