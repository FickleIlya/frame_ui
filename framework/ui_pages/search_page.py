from typing import Optional

import allure
from selene.browser import open_url
from selene.support.jquery_style_selectors import s
from selenium.webdriver.support.ui import Select


class SearchPage:

    def __init__(self):
        # inputs
        self.movie_title = s('#find_film')
        self.year = s('#year')
        self.actor = s('#formSearchMain > input.text.el_9')
        self.creator = s('#formSearchMain > input.text.el_10')

        # selects
        self.select_country = s('#country')
        self.select_year_start = s('#from_year')
        self.select_year_end = s('#to_year')
        self.select_distributor = s('#company')
        self.select_mpaa = s('#formSearchMain > select.text.el_8')

        # premiere selects
        self.select_premiere_month = s('#prem_month')
        self.select_premiere_year = s('#prem_year')
        self.select_premiere_where = s('#prem_type')

        # gengre select
        self.select_genre = s('#m_act\[genre\]')

        # fees select
        self.select_fees_ge_or_le = s('#formSearchMain > select.text.el_14')
        self.select_fees_money = s('#formSearchMain > input.text.el_15')
        self.select_fees_where = s('#formSearchMain > input.text.el_16')

        # what to look for? select
        self.select_look_for = s('#formSearchMain > select.text.el_17')

        # search nice button
        self.search_button = s('#formSearchMain > input.el_18.submit.nice_button')

    def open(self):
        open_url('/')
        return self

    @allure.step("Найти")
    def search(self, movie_title: Optional[str] = "", year: Optional[str] = "", year_start: Optional[str] = None,
               year_end: Optional[str] = None, country: Optional[str] = None, distributor: Optional[str] = None,
               mpaa: Optional[str] = None, genre: Optional[str] = None, actor: Optional[str] = "",
               creator: Optional[list] = "", premiere: Optional[list] = None, fees: Optional[list] = None):

        self.movie_title.set(movie_title)
        self.year.set(year)
        self.actor.set(actor)
        self.creator.set(creator)
        if country:
            select = Select(self.select_country)
            select.select_by_visible_text(country)
        if year_start:
            select = Select(self.select_year_start)
            select.select_by_visible_text(year_start)
        if year_end:
            select = Select(self.select_year_end)
            select.select_by_visible_text(year_end)
        if distributor:
            select = Select(self.select_distributor)
            select.select_by_visible_text(distributor)
        if mpaa:
            select = Select(self.select_mpaa)
            select.select_by_visible_text(mpaa)
        if genre:
            select = Select(self.select_genre)
            select.select_by_visible_text(genre)
        if premiere:
            select_month = Select(self.select_premiere_month)
            select_month.select_by_visible_text(premiere[0])
            select_year = Select(self.select_premiere_year)
            select_year.select_by_visible_text(premiere[1])
            select_where = Select(self.select_premiere_where)
            select_where.select_by_visible_text(premiere[2])
        if fees:
            select_ge_or_le = Select(self.select_fees_ge_or_le)
            select_ge_or_le.select_by_visible_text(premiere[0])
            select_money = Select(self.select_fees_money)
            select_money.select_by_visible_text(premiere[1])
            select_where = Select(self.select_fees_where)
            select_where.select_by_visible_text(premiere[2])

        self.search_button.click()
