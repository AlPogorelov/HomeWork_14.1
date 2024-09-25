from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        summ_product = 0
        for product in self.__products:
            summ_product += product.quantity
        return f"{self.name}, количества продуктов: {summ_product} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product):
        if isinstance(product, Product):
            Category.product_count += 1
            return self.__products.append(product)

        raise TypeError

    @property
    def product_list(self):
        return self.__products
