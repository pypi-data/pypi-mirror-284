from setuptools import setup, find_packages

setup(
    name="pyf_pagination",
    version="0.0.4",
    packages=find_packages(include=["pagination", "pagination.*"]),
    install_requires=[
        "djangorestframework",
    ],
    author="ycx",
    author_email="ycx3030@126.com",
    description="A pagination package for Django REST Framework",
    url="https://github.com/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
)
