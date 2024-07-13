from setuptools import setup, find_packages

setup(
    name='PCreate',
    version='0.1',
    description='A package to quickly initialize Python projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sarthak Walia',
    author_email='waliasarthak0009@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pcreate=pcreate.create_project:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
