import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфон"
    assert first_category.description == "Смартфоны"
    assert len(first_category.product_list) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_category_add_product_property(first_category):
    assert first_category.products == "Samsung, 180000.0 руб. Остаток: 3 шт.\n"


def test_category_add_product_setter(first_category, product):
    assert len(first_category.product_list) == 1
    first_category.add_product(product)
    assert len(first_category.product_list) == 2


def test_category_str(first_category):
    assert str(first_category) == "Смартфон, количества продуктов: 3 шт."


def test_category_add_product(first_category, product_smartphone1):
    assert len(first_category.product_list) == 1
    first_category.add_product(product_smartphone1)
    assert len(first_category.product_list) == 2


def test_category_add_product_error(first_category):
    assert len(first_category.product_list) == 1
    with pytest.raises(TypeError):
        first_category.add_product('No product')

    assert len(first_category.product_list) == 1
