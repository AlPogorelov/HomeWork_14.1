from src.product import Product
def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "WIFI"
    assert product.price == 180000.0
    assert product.quantity == 2

def test_new_product():
    add_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                       "price": 180000.0, "quantity": 5})
    assert add_product.name == "Samsung Galaxy S23 Ultra"
    assert add_product.description == "256GB, Серый цвет, 200MP камера"
    assert add_product.price == 180000.0
    assert add_product.quantity == 5

def test_price_property(product):
    assert product.price == 180000.0

def test_price_setter(product):
    product.price = 100
    assert product.price == 100

