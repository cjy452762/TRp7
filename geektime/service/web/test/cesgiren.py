from selenium import webdriver


class Ceshiren:
    def open(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # 进入网站
        self.driver.get('https://ceshiren.com/')
    def search(self, keyword):
        ...

    def clear(self):
        ...
