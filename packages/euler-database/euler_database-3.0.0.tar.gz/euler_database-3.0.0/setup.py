from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="euler_database",
    version="3.0.0",
    author="Prashant Verma",
    author_email="prashant27050@gmail.com",
    description="A graph database application with embedding and similarity calculations.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['icons/*.png', 'fonts/fa-solid-900.ttf'],  # Include .png and .ttf files
        'euler_database': ['icons/*.png', 'fonts/fa-solid-900.ttf'],  # Ensure correct package path
    },
    install_requires=[
        "numpy",
        "scikit-learn",
        "torch",
        "Pillow",
        "customtkinter",
        "node2vec"
    ],
    entry_points={
        'console_scripts': [
            'eulerdb=gui.app:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
