import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def first_category():
    return Category(
        name='Смартфон',
        description="Смартфоны",
        products=[
            Product("Samsung", "256GB", 180000.0, 3)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name='Телевизор',
        description="Телефизор",
        products=[
            Product("Samsung", "WIFI", 180000.0, 2),
            Product("LG", "Android", 200000.0, 1)
        ]
    )

@pytest.fixture
def product():
    return Product("Samsung", "WIFI", 180000.0, 2)
