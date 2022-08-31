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
        final_page = search_page.search(movie_title=self.search_data.movie_title,
                                        year=self.search_data.year,
                                        actor=self.search_data.actor,
                                        country=self.search_data.country)
