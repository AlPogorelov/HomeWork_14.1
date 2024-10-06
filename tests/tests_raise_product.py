import pytest

from src.product import Product


def test_raise_zero_quantity():
    with pytest.raises(ValueError):
        Product("Samsung", "WIFI", 180000.0, 0)
