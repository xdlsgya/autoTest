#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

url='http://20.26.38.43:9999/aicas/login?service=http%3A%2F%2F20.26.38.43%3A9999%2Facam%2Fpage%2Fapp.jsp#/iframe/25020033'
username='admin'
passwd='!qaz2wsx5'

driver = webdriver.Chrome()
driver.get(url)

ele_user = driver.find_element_by_xpath('//*[@id="username"]')
ele_user.clear()
ele_user.send_keys(username)
ele_pass = driver.find_element_by_xpath('//*[@id="password"]')
ele_pass.clear()
ele_pass.send_keys(passwd)
ele_commit = driver.find_element_by_xpath('//*[@id="loginButton"]').click()#

driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/li[3]').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/li[1]').click()


input_ele = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/form/div/div[1]/div/div/div/input')
input_ele.clear()

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/form/div/div[1]/div/div/div/input[@placeholder="请输入内容"]')

driver.find_element_by_class_name("el-input__inner")

# el = driver.find_element_by_xpath("//input[@placeholder='请通过XPATH定位元素']")




<div class="el-input el-input--small">
	<input type="text" autocomplete="off" placeholder="请输入内容" class="el-input__inner">
</div>