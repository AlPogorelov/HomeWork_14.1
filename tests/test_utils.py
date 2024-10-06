import os

from src.product import Product
from src.utils import open_json, create_from_json
from tests.conftest import data_json

file_name = './tests/test_products.json'


def test_open_json(data_json):
    full_file_name = os.path.abspath(file_name)
    assert open_json(file_name) == data_json
