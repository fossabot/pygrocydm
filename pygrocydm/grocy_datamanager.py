from .battery import BATTERIES_ENDPOINT, Battery
from .chore import CHORES_ENDPOINT, Chore
from .grocy_api_client import (DEFAULT_PORT_NUMBER, GrocyApiClient,
                               GrocyEntityList)
from .location import LOCATION_ENDPOINT, Location
from .product import PRODUCTS_ENDPOINT, Product
from .product_group import PRODUCT_GROUPS_ENDPOINT, ProductGroup
from .quantity_unit import QUANTITY_UNITS_ENDPOINT, QuantityUnit
from .shopping_list import (SHOPPING_LIST_ENDPOINT, SHOPPING_LISTS_ENDPOINT,
                            ShoppingList, ShoppingListItem)
from .task import TASKS_ENDPOINT, Task
from .task_category import TASK_CATEGORIES_ENDPOINT, TaskCategory


class GrocyDataManager():
    def __init__(
            self, base_url, api_key,
            port: int = DEFAULT_PORT_NUMBER,
            verify_ssl=True):
        self.__api = GrocyApiClient(base_url, api_key, port, verify_ssl)

    def products(self) -> GrocyEntityList:
        cls = Product
        return GrocyEntityList(self.__api, cls, PRODUCTS_ENDPOINT)

    def chores(self) -> GrocyEntityList:
        cls = Chore
        return GrocyEntityList(self.__api, cls, CHORES_ENDPOINT)

    def locations(self) -> GrocyEntityList:
        cls = Location
        return GrocyEntityList(self.__api, cls, LOCATION_ENDPOINT)

    def batteries(self) -> GrocyEntityList:
        cls = Battery
        return GrocyEntityList(self.__api, cls, BATTERIES_ENDPOINT)

    def shopping_list(self) -> GrocyEntityList:
        cls = ShoppingListItem
        return GrocyEntityList(self.__api, cls, SHOPPING_LIST_ENDPOINT)

    def shopping_lists(self) -> GrocyEntityList:
        cls = ShoppingList
        return GrocyEntityList(self.__api, cls, SHOPPING_LISTS_ENDPOINT)

    def quantity_units(self) -> GrocyEntityList:
        cls = QuantityUnit
        return GrocyEntityList(self.__api, cls, QUANTITY_UNITS_ENDPOINT)

    def tasks(self) -> GrocyEntityList:
        cls = Task
        return GrocyEntityList(self.__api, cls, TASKS_ENDPOINT)

    def task_categories(self) -> GrocyEntityList:
        cls = TaskCategory
        return GrocyEntityList(self.__api, cls, TASK_CATEGORIES_ENDPOINT)

    def product_groups(self) -> GrocyEntityList:
        cls = ProductGroup
        return GrocyEntityList(self.__api, cls, PRODUCT_GROUPS_ENDPOINT)
