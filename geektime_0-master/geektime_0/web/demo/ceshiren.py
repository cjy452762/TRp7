from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.demo.search import Search


class Ceshiren:
    def open(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        self.driver.get('https://ceshiren.com/')

    def open_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        search=Search(self.driver)
        return search

