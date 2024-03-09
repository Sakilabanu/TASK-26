from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"
        self.search_box = (By.ID, "name")
        self.birth_month_dropdown = (By.ID, "birth_month")
        self.birth_day_input = (By.ID, "birth_day")
        self.birth_year_input = (By.ID, "birth_year")
        self.gender_dropdown = (By.ID, "gender")
        self.search_button = (By.ID, "search")

    def navigate_to_page(self):
        self.driver.get(self.url)

    def fill_search_criteria(self, name, birth_month, birth_day, birth_year, gender):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_box)).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.birth_month_dropdown)).send_keys(birth_month)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.birth_day_input)).send_keys(birth_day)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.birth_year_input)).send_keys(birth_year)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.gender_dropdown)).send_keys(gender)

    def click_search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()
