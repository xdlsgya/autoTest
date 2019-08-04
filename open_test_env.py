# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#unittest为python中的单元测试框架
class UntitledTestCase(unittest.TestCase):
    #设置初始化部分，在用例执行前事先被调用
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一个警告。
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://20.26.38.43:9999/aicas/login?service=http://20.26.38.43:9999/acam")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("!qaz2wsx5")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=username | ]]
        driver.find_element_by_id("loginButton").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/li/div/span[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/li/ul/li").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("!qaz2wsx5")
    
    #查找页面元素是否存在，此函数用处不大，通常删除
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    #对弹窗异常的处理
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    #关闭警告以及对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    #最后执行，一般做清理工作，如退出浏览器等
    def tearDown(self):
        self.driver.quit()
        #断言，对前面 verificationErrors 方法获得的列表进行比较;如查 verificationErrors 的列表不为空，输出列表中的报错信息。
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
