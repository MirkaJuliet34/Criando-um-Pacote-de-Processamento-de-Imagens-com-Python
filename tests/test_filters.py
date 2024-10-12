# tests/test_filters.py
import pytest
from PIL import Image
from image_processing.filters import apply_blur, apply_contour

@pytest.fixture
def sample_image():
    """Cria uma imagem de exemplo para usar nos testes."""
    return Image.new("RGB", (100, 100), color="red")  # Imagem vermelha de 100x100

def test_apply_blur(sample_image):
    """Testa se o filtro de desfoque é aplicado corretamente."""
    blurred_image = apply_blur(sample_image)
    
    # Verifica se o tipo de retorno é uma imagem
    assert isinstance(blurred_image, Image.Image)
    
    # Não temos uma forma direta de verificar o desfoque, mas podemos verificar que o objeto retornado é diferente
    assert blurred_image != sample_image

def test_apply_contour(sample_image):
    """Testa se o filtro de contorno é aplicado corretamente."""
    contoured_image = apply_contour(sample_image)
    
    # Verifica se o tipo de retorno é uma imagem
    assert isinstance(contoured_image, Image.Image)
    
    # Verifica que o objeto retornado é diferente da imagem original
    assert contoured_image != sample_image
