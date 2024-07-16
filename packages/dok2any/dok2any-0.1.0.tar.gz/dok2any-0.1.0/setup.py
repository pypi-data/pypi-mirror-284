from setuptools import setup, find_packages

setup(
    name="dok2any",
    version="0.1.0",
    author="Dulaj Ramanayaka",
    author_email="dulajnr97git@gmail.com",
    description="A package to convert DOK files to various formats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dulaanr97/dok2any",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "openbabel",
    ],
    entry_points={
        "console_scripts": [
            "dok2any=dok2any.converter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)

