from setuptools import setup, find_packages

setup(
    name="hey_mohamed",
    version="0.1.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple project to greet Mohamed",
    long_description="This is a simple project to demonstrate how to create a Python package",
    long_description_content_type="text/markdown",
    url="https://github.com/osharif123/hey_mohamed",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hey_mohamed=hey_mohamed.main:greet',
        ],
    },
)