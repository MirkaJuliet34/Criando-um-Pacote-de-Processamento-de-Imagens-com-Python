# image_processing/transformations.py
from PIL import Image

def resize_image(image: Image, size: tuple) -> Image:
    """Redimensiona a imagem para o tamanho especificado."""
    return image.resize(size)

def rotate_image(image: Image, angle: int) -> Image:
    """Rotaciona a imagem pelo ângulo especificado."""
    return image.rotate(angle)
