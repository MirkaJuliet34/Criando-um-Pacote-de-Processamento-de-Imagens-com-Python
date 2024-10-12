# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image_processing_package",
    version="0.1.0",
    author="Seu Nome",
    author_email="seu_email@example.com",
    description="Pacote para processamento básico de imagens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/image-processing-package",
    packages=find_packages(),
    install_requires=["Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
