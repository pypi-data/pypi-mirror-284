# sel_auto_base.py

from selenium import webdriver


class SeleniumBase:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def close_browser(self):
        self.driver.quit()
