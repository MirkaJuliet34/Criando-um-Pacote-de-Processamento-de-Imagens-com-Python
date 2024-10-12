# image_processing/filters.py
from PIL import Image, ImageFilter

def apply_blur(image: Image) -> Image:
    """Aplica um filtro de desfoque na imagem."""
    return image.filter(ImageFilter.BLUR)

def apply_contour(image: Image) -> Image:
    """Aplica um filtro de contorno na imagem."""
    return image.filter(ImageFilter.CONTOUR)
