from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search:
    def __init__(self, driver):
        self.driver=driver

    def search(self, keyword) -> str:
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'topic-title'))
        )
        return self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()

    def clear_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="清除搜索内容"]').click()

    def filter(self, tags=[], subject_type=None, range=None):
        ...
