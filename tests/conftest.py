import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_category():
    return Category(
        name="Смартфон",
        description="Смартфоны",
        products=[Product("Samsung", "256GB", 180000.0, 3)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизор",
        description="Телефизор",
        products=[
            Product("Samsung", "WIFI", 180000.0, 2),
            Product("LG", "Android", 200000.0, 1),
        ],
    )


@pytest.fixture
def product():
    return Product("Samsung", "WIFI", 180000.0, 2)


@pytest.fixture
def sec_product():
    return Product("LG", "Android", 200000.0, 1)


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)
