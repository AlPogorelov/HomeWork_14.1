import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.product import Smartphone
from src.product import LawnGrass


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


@pytest.fixture
def product_smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 200.0, 2, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 100.0, 2, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 2, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 200.0, 2, "США", "5 дней", "Темно-зеленый")

@pytest.fixture
def zero_list_category():
    return Category(
        name="Смартфон",
        description="Смартфоны",
        products=[],
    )

