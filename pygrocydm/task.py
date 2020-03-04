from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_date, parse_int, parse_bool

TASKS_ENDPOINT = 'objects/tasks'


class Task(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__due_date = parse_date(parsed_json.get('due_date', None))
        self.__done = parse_bool(parsed_json.get('done'), False)
        self.__done_timestamp = parse_date(parsed_json.get('done_timestamp', None))
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__category_id = parse_int(parsed_json.get('category_id'), None)
        self.__assigned_to_user_id = parse_int(parsed_json.get('assigned_to_user_id'))
        self.__endpoint = '{}/{}'.format(TASKS_ENDPOINT, self.__id)
        super().__init__(api, self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def due_date(self) -> datetime:
        return self.__due_date

    @property
    def done(self) -> bool:
        return self.__done

    @property
    def done_timestamp(self) -> datetime:
        return self.__done_timestamp

    @property
    def category_id(self) -> int:
        return self.__category_id

    @property
    def assigned_to_user_id(self) -> int:
        return self.__assigned_to_user_id

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
