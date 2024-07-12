from setuptools import setup, find_packages

setup(
    name='myphonebook',  # Updated package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'myphonebook=myphonebook.cli:main',  # Updated entry point
        ],
    },
    author='Atif Ghafoor',
    author_email='atifghafoor377@gmail.com',
    description='A CLI application for managing a phonebook',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/atif-ghafoor/myphonebook',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
