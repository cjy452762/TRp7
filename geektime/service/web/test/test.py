import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # 进入网站
        self.driver.get('https://ceshiren.com/')

    def setup(self):
        self.driver.find_element(By.ID, 'search-button').click()

    def teardown(self):
        self.driver.find_element(By.ID, 'search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="清除搜索内容"]')

    @pytest.mark.parametrize("keyword", [
        'selenium',
        'appium',
    ])
    def test_search(self, keyword):
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
        # 判断结果
        assert keyword in self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()
