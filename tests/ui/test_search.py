from pprint import pprint

import allure
import pytest

from framework.resources.test_params.search_data import BaseSearchData
from framework.ui_pages.search_page import SearchPage


@pytest.mark.positive
@pytest.mark.usefixtures('allure_screen')
@allure.feature('Kinopoisk.ru поиск')
class TestSearch:
    search_data = BaseSearchData

    @allure.story('Выполнение поиска')
    @allure.testcase('https://www.kinopoisk.ru/s', name='тест')
    @pytest.mark.usefixtures("close_driver_after_test")
    def test_search_movie(self):
        """
        Описание теста.
        Произвести поиск на сайте https://www.kinopoisk.ru/s/ по заданным параметрам
        """
        search_page = SearchPage().open()
        final_page = search_page.search(movie_title=self.search_data.movie_title, year=self.search_data.year,
                                        year_start=self.search_data.year_start, year_end=self.search_data.year_end,
                                        country=self.search_data.country, distributor=self.search_data.distributor,
                                        mpaa=self.search_data.mpaa, genre=self.search_data.genre,
                                        actor=self.search_data.actor, creator=self.search_data.creator,
                                        premiere=self.search_data.premiere, fees=self.search_data.fees)

        assert self.search_data.result_movie in final_page.films_list
