class Category:
    name: str
    description: str
    product: list
    count_category = 0
    len_product = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.product = products if products else []
        Category.count_category += 1
        Category.len_product += len(products)
