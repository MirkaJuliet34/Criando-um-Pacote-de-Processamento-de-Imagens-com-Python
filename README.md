# Image Processing Package

Este é um pacote Python para aplicar filtros e transformações em imagens utilizando a biblioteca Pillow.

## Instalação

```bash
pip install image-processing-package

```
## Funcionalidades

- apply_blur(image): Aplica um filtro de desfoque na imagem.
- resize_image(image, size): Redimensiona a imagem para um tamanho especificado.

## Exemplo de uso

```from image_processing_package.filters import apply_blur
from PIL import Image

# Carregar imagem
image = Image.open('imagem.jpg')

# Aplicar desfoque
blurred_image = apply_blur(image)
blurred_image.show()
```
### **Passo 5: Criando Distribuições** 📦

Certifique-se de ter o `setuptools`, `wheel` e `twine` instalados:

```bash
python -m pip install --upgrade pip
python -m pip install --user setuptools wheel twine
```
### Crie as distribuições

```
python setup.py sdist bdist_wheel

```

### Publicando no Test PyPI 🗂️

Crie uma conta no Test PyPI:

- Test PyPI Register

Depois de criar a conta, faça o upload do pacote:

```
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Teste a instalação do pacote no Test PyPI:

```
pip install --index-url https://test.pypi.org/simple/ image-processing-package
```
### Publicando no PyPI Oficial 🌍

Crie uma conta no PyPI:

- PyPI Register

Depois de registrado, suba o pacote no PyPI oficial:

```
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
Agora, qualquer pessoa pode instalar o seu pacote diretamente do PyPI:

```
pip install image-processing-package
```
