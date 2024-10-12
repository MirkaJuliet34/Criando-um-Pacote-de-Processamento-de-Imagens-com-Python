# tests/test_transformations.py
import pytest
from PIL import Image
from image_processing.transformations import resize_image, rotate_image

@pytest.fixture
def sample_image():
    """Cria uma imagem de exemplo para usar nos testes."""
    return Image.new("RGB", (100, 100), color="blue")  # Imagem azul de 100x100

def test_resize_image(sample_image):
    """Testa se a função de redimensionamento altera o tamanho da imagem corretamente."""
    new_size = (50, 50)
    resized_image = resize_image(sample_image, new_size)
    
    # Verifica se o tipo de retorno é uma imagem
    assert isinstance(resized_image, Image.Image)
    
    # Verifica se o tamanho da imagem foi alterado
    assert resized_image.size == new_size

def test_rotate_image(sample_image):
    """Testa se a função de rotação rotaciona a imagem corretamente."""
    angle = 90
    rotated_image = rotate_image(sample_image, angle)
    
    # Verifica se o tipo de retorno é uma imagem
    assert isinstance(rotated_image, Image.Image)
    
    # Verifica se a rotação foi aplicada (podemos verificar se a imagem mudou)
    assert rotated_image != sample_image
