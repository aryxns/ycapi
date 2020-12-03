import requests
#from requests import Session
from models import Item, User
from const import API_PATH, BASE_PATH, DEFAULT_LIMIT, ITEM_BASE_URL, USER_BASE_URL


class HackerNews:
    def __init__(self, base_path=BASE_PATH, session=None):
        self.base_path = base_path
        self.session = requests
    
    def get(self, path):
        return self.session.get('/'.join((self.base_path, path))).json()
    
    def item(self, id_):
        return Item(id_, self)

    def iterate_list(self, items, limit):
        items = iter(items)
        i = 0
        for item in items:
            if limit is None or i < limit:
                yield self.item(item)
                i += 1
            else:
                break
    
    def jobs(self, limit=DEFAULT_LIMIT):
        return self.iterate_list(self.get(API_PATH['job']), limit)

    def user(self, name):
        return User(name, self)