from setuptools import setup, find_packages

setup(
    name='softpro_elk_grpc_logger',
    version='0.1.0',
    author='Verenych Danylo',
    author_email="karate3@gmail.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description='A small package for ELK structure logging for python microservices',
    url="https://git.softpro.ua/service/python_logger",
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
    install_requires=[
    ]
)