from datetime import datetime
from typing import List

from .product import Product
from .grocy_api_client import DEFAULT_PORT_NUMBER, GrocyApiClient


class GrocyDataManager(object):
    def __init__(self, base_url, api_key, port: int = DEFAULT_PORT_NUMBER, verify_ssl=True):
        self.__api = GrocyApiClient(base_url, api_key, port, verify_ssl)

    def products(self) -> List[Product]:
        endpoint = 'objects/products'
        parsed_json = self.__api.get_request(endpoint)
        return [Product(response, self.__api) for response in parsed_json] 
