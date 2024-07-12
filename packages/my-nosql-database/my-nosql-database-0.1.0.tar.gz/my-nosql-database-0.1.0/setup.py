from setuptools import setup, find_packages

setup(
    name="my-nosql-database",
    version="0.1.0",
    author="Manupal Choudhary",
    author_email="hi@manupal.dev",
    description="A simple NoSQL database using SQLite as the underlying storage engine",
    url="https://manupal.dev/project/my-nosql-database",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
