# setup.py

from setuptools import setup, find_packages

setup(
    name="replica_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "diffusers",
    ],
    author="Kushagra Vyas",
    author_email="vyaskushagra2003@gmail.com",
    description="A library to generate replica images using Hugging Face models.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kushcoder12/Replica-Generator",  # Update with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
