from setuptools import setup, find_packages

setup(
    name="pyf_pagination",
    version="0.0.2",
    packages=find_packages(),  # 自动找到所有包含的包
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
