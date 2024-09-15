import json
import os.path

from src.category import Category
from src.product import Product


def open_json(file_name):
    full_file_name = os.path.abspath(file_name)
    with open(full_file_name, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_from_json(data):
    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))

        category["products"] = products

        categorys.append(Category(**category))
    return categorys
