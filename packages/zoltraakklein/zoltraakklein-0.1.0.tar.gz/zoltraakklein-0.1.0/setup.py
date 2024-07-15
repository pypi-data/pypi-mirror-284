from setuptools import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zoltraakklein",
    version="0.1.0",
    author="Daisuke Yamaguchi",
    author_email="daicom0204@gmail.com",
    description="A simplified zoltraak class.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Habatakurikei/zoltraakklein",
    package_data={'': ['*']},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "llmmaster>=0.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=6.0",
        ],
    },
)
