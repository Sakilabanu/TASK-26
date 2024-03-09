# tests/test_imdb_search.py

import pytest
from selenium import webdriver
from page_objects.imdb_search_page import IMDbSearchPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_imdb_search(setup):
    imdb_search_page = IMDbSearchPage(setup)
    imdb_search_page.navigate_to_page()
    imdb_search_page.fill_search_criteria("John Doe", "January", "1", "1980", "Male")
    imdb_search_page.click_search_button()

    # Add assertions to verify search results or perform further actions