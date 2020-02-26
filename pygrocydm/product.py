from .utils import parse_date, parse_float, parse_int, parse_bool
from typing import List
from datetime import datetime
from .grocy_api_client import GrocyApiClient, GrocyEntity

PRODUCTS_ENDPOINT = 'objects/products'

class Product(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__location_id = parse_int(parsed_json.get('location_id', None))
        self.__qu_id_purchase = parse_int(parsed_json.get('qu_id_purchase', None))
        self.__qu_id_stock = parse_int(parsed_json.get('qu_id_stock', None))
        self.__enable_tare_weight_handling = parse_int(parsed_json.get('enable_tare_weight_handling', None))
        self.__not_check_stock_fulfillment_for_recipes = parse_int(parsed_json.get('not_check_stock_fulfillment_for_recipes'), None)
        self.__product_group_id = parse_int(parsed_json.get('product_group_id'))
        self.__qu_factor_purchase_to_stock = parse_float(parsed_json.get('qu_factor_purchase_to_stock', None))
        self.__tare_weight = parse_float(parsed_json.get('tare_weight', None))
        barcodes_raw = parsed_json.get('barcode', "")
        if barcodes_raw:
            self.__barcodes = barcodes_raw.split(",")
        else:
            self.__barcodes = None
        self.__min_stock_amount = parse_int(parsed_json.get('min_stock_amount', None), 0)
        self.__default_best_before_days = parse_int(parsed_json.get('default_best_before_days', None))
        self.__default_best_before_days_after_open = parse_int(parsed_json.get('default_best_before_days_after_open', None))
        self.__picture_file_name = parsed_json.get('picture_file_name', None)
        self.__allow_partial_units_in_stock = parse_int(parsed_json.get('allow_partial_units_in_stock', False), False)
        self.__row_created_timestamp = parse_date(parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(PRODUCTS_ENDPOINT, self.__id)
        super().__init__(api, self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def product_group_id(self) -> int:
        return self.__product_group_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def barcodes(self) -> List[str]:
        return self.__barcodes

    @property
    def location_id(self) -> int:
        return self.__location_id

    @property
    def qu_id_purchase(self) -> int:
        return self.__qu_id_purchase

    @property
    def description(self) -> str:
        return self.__description

    @property
    def qu_id_stock(self) -> int:
        return self.__qu_id_stock

    @property
    def enable_tare_weight_handling(self) -> int:
        return self.__enable_tare_weight_handling

    @property
    def not_check_stock_fulfillment_for_recipes(self) -> int:
        return self.__not_check_stock_fulfillment_for_recipes

    @property
    def qu_factor_purchase_to_stock(self) -> float:
        return self.__qu_factor_purchase_to_stock

    @property
    def tare_weight(self) -> float:
        return self.__tare_weight

    @property
    def min_stock_amount(self) -> int:
        return self.__min_stock_amount

    @property
    def default_best_before_days(self) -> int:
        return self.__default_best_before_days

    @property
    def default_best_before_days_after_open(self) -> int:
        return self.__default_best_before_days_after_open

    @property
    def picture_file_name(self) -> str:
        return self.__picture_file_name

    @property
    def allow_partial_units_in_stock(self) -> int:
        return self.__allow_partial_units_in_stock

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
