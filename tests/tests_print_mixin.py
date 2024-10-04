from src.product import Product, Smartphone


def test_print_mixin(capsys):
    Product("Samsung", "WIFI", 180000.0, 2)
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Product(Samsung, WIFI, 180000.0, 2)'

    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 200.0, 2, 95.5,
               "S23 Ultra", 256, "Серый")
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 200.0, 2)'
