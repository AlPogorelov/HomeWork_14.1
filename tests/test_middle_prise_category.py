def test_middle_price(second_category):
    assert second_category.middle_price() == 190000.0


def test_middle_price_with_zero_product_list(zero_list_category):
    assert zero_list_category.middle_price() == 0
