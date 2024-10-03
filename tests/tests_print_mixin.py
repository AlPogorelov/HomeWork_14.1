from src.product import Product


def test_print_mixin(capsys):
    Product("Samsung", "WIFI", 180000.0, 2)
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Product(Samsung, WIFI, 180000.0, 2)'
