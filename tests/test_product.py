import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "WIFI"
    assert product.price == 180000.0
    assert product.quantity == 2


def test_new_product():
    add_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    assert add_product.name == "Samsung Galaxy S23 Ultra"
    assert add_product.description == "256GB, Серый цвет, 200MP камера"
    assert add_product.price == 180000.0
    assert add_product.quantity == 5


def test_price_property(product):
    assert product.price == 180000.0


def test_price_setter(product):
    product.price = 100
    assert product.price == 100


def test_product_str(product):
    assert str(product) == "Samsung, 180000.0 руб. Остаток: 2 шт."


def test_total_sum_price_product(product, sec_product):
    assert product + sec_product == 560000.0


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung"
    assert next(product_iterator).name == "LG"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_init_smartphone(product_smartphone1):
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_init_lawngrass(product_lawngrass1):
    assert product_lawngrass1.name == "Газонная трава"
    assert product_lawngrass1.country == "Россия"
    assert product_lawngrass1.germination_period == "7 дней"
    assert product_lawngrass1.color == "Зеленый"


def test_product_smartphone_add(product_smartphone1, product_smartphone2):
    assert product_smartphone1 + product_smartphone2 == 600.0


def test_product_lawngrass_add(product_lawngrass1, product_lawngrass2):
    assert product_lawngrass1 + product_lawngrass2 == 1400.0


def test_product_add_error(product_smartphone1, product_lawngrass1):
    with pytest.raises(TypeError):
        product_smartphone1 + product_lawngrass1
