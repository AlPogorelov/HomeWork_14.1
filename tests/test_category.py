
def test_category_init(first_category, second_category):
    assert first_category.name == 'Смартфон'
    assert first_category.description == 'Смартфоны'
    assert len(first_category.product_list) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3

def test_category_add_product_property(first_category):
    assert first_category.add_product == 'Samsung, 180000.0 руб. Остаток: 3 шт.\n'

def test_category_add_product_setter(first_category, product):
    assert len(first_category.product_list) == 1
    first_category.add_product = product
    assert len(first_category.product_list) == 2