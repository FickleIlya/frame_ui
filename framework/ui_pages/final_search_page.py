from pprint import pprint

from selene.support import by
from selene.support.jquery_style_selectors import s, ss


class FinalPage:
    def __init__(self):
        films_list = ss(by.xpath('//*[@id="block_left_pad"]/div/div/div/div[2]/p/a'))
        self._films_list = [film.text for film in films_list][:5]

    @property
    def films_list(self):
        return self._films_list
