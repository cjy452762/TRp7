import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime.service.web.test.cesgiren import Ceshiren


class TestCeshiren:
    def setup_class(self):
        ceshiren=Ceshiren()
        ceshiren.open()


    def setup(self):
        self.driver.find_element(By.ID, 'search-button').click()

    def teardown(self):
        self.driver.find_element(By.ID, 'search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="清除搜索内容"]')

    @pytest.mark.parametrize("keyword", [
        '自动化测试',
        'appium',
    ])
    def test_search(self, keyword):
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
        #等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'topic-title')))
        # 判断结果
        assert keyword in self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()
