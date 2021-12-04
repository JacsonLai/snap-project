import time

from selenium import webdriver

# 如果firefox没有安装在默认位置，就要手动指定位置
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

def login_module(brower, name, passwd):
    ti_login = driver.find_element_by_xpath('//*[@id="tiResponsiveHeader"]/div/div[2]/div[2]/div[1]/ti-login')
    ti_login.click()
    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)

    while True:
        try:
            driver.find_element_by_name('username')
            break
        except NoSuchElementException:
            print("username元素找不到")
        except TimeoutException:
            print("Time out")
    # ti登陆
    userName = driver.find_element_by_name('username')
    # userName.send_keys(name)
    for i in list(name):
        userName.send_keys(i)
        time.sleep(0.5)
    # time.sleep(3)
    next_button = driver.find_element_by_id('nextbutton')
    next_button.click()
    password = driver.find_elements_by_name('password')

    # password[1].send_keys(passwd)
    for i in list(passwd):
        password[1].send_keys(i)
        time.sleep(0.5)
    # time.sleep(3)
    login_button = driver.find_element_by_name('loginbutton')
    # time.sleep(3)
    login_button.click()

def addcart_module(brower):
    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="quicklink_cart"]')
            break
        except NoSuchElementException:
            print("quickcart元素找不到")
        except TimeoutException:
            print("Time out")
    cart = driver.find_element_by_xpath('//*[@id="quicklink_cart"]')
    # cart = a_href[0]
    # for i in a_href:
    #     if i.get_attribute("href") == "https://www.ti.com.cn/zh-cn/ordering-resources/buying-tools/quick-add-to-cart.html":
    #         cart = i
    #         break
    cart.click()

    while True:
        try:
            driver.find_elements_by_tag_name("table")
            break
        except NoSuchElementException:
            print("cart元素找不到")
        except TimeoutException:
            print("Time out")

    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)
    # driver.implicitly_wait(2)
    table = driver.find_elements_by_tag_name("table")
    print(len(table))
    throws = table[0].find_elements_by_tag_name("tr")
    print(len(throws))
    td = throws[1].find_elements_by_tag_name("td")
    print(len(td))
    device_input = td[1].find_element_by_tag_name("ti-input")
    # print(len(device_input))
    device_input.click()
    device_value = ['N', 'E', '5', '5', '5', 'D', 'R']
    for i in device_value:
        device_input.send_keys(i)
        time.sleep(0.5)
    td[4].click()
    # time.sleep(2)
    num_input = td[3].find_element_by_tag_name("ti-input")
    # time.sleep(4)

    # time.sleep(2)
    num_input.click()
    while True:
        kucun = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/table/tbody/tr[1]/td[5]')
        if kucun.text != "":
            print(kucun.text)
            break
    num_input.click()
    num_input.send_keys('1')
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH,
                                                                     '/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/div[2]/ti-button'))).click()

name = '641896601@qq.com'
passwd = 'Zwylisy33'
location = 'E:/firefox75/firefox.exe'
options = webdriver.FirefoxOptions()
options.set_capability("marionette", False)
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-infobars")
# options.add_argument("ignore-certificate-errors")
options.set_preference("dom.webdriver.enabled", False)
# profile = webdriver.FirefoxProfile('C:/Users/nero/AppData/Roaming/Mozilla/Firefox/Profiles/2az14d6y.default-release')
profile = webdriver.FirefoxProfile()
# ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# profile.set_preference("general.useragent.override", ua)
PROXY_HOST = "12.12.12.123"
PROXY_PORT = "1234"
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
profile.set_preference("dom.webdriver.enabled", False)  # 设置非driver驱动
profile.set_preference('useAutomationExtension', False) #关闭自动化提示
profile.update_preferences()    #更新设置
desired = DesiredCapabilities.FIREFOX
driver = webdriver.Firefox(firefox_binary=location, firefox_profile=profile, options=options, desired_capabilities=desired)

# 请求页面
# driver.implicitly_wait(16)
driver.delete_all_cookies()
driver.get("https://www.ti.com/")

# ti_login = driver.find_element_by_xpath('//*[@id="tiResponsiveHeader"]/div/div[2]/div[2]/div[1]/ti-login')
# ti_login.click()
# allhandles = driver.window_handles
# for handle in allhandles:
#     driver.switch_to.window(handle)
#     print(driver.current_url)
#
#
# while True:
#     try:
#         driver.find_element_by_name('username')
#         break
#     except NoSuchElementException:
#         print("username元素找不到")
#     except TimeoutException:
#         print("Time out")
# # ti登陆
# userName = driver.find_element_by_name('username')
# userName.send_keys(name)
# # time.sleep(3)
# next_button = driver.find_element_by_id('nextbutton')
# next_button.click()
# password = driver.find_elements_by_name('password')
#
# password[1].send_keys(passwd)
# # time.sleep(3)
# login_button = driver.find_element_by_name('loginbutton')
# time.sleep(3)
# login_button.click()
#
# time.sleep(2)
# while True:
#     try:
#         driver.find_element_by_xpath('//*[@id="quicklink_cart"]')
#         break
#     except NoSuchElementException:
#         print("quickcart元素找不到")
#     except TimeoutException:
#         print("Time out")
# cart = driver.find_element_by_xpath('//*[@id="quicklink_cart"]')
# # cart = a_href[0]
# # for i in a_href:
# #     if i.get_attribute("href") == "https://www.ti.com.cn/zh-cn/ordering-resources/buying-tools/quick-add-to-cart.html":
# #         cart = i
# #         break
# cart.click()
#
# while True:
#     try:
#         driver.find_elements_by_tag_name("table")
#         break
#     except NoSuchElementException:
#         print("cart元素找不到")
#     except TimeoutException:
#         print("Time out")
#
# allhandles = driver.window_handles
# for handle in allhandles:
#     driver.switch_to.window(handle)
#     print(driver.current_url)
# # driver.implicitly_wait(2)
# table = driver.find_elements_by_tag_name("table")
# print(len(table))
# throws = table[0].find_elements_by_tag_name("tr")
# print(len(throws))
# td = throws[1].find_elements_by_tag_name("td")
# print(len(td))
# device_input = td[1].find_element_by_tag_name("ti-input")
# # print(len(device_input))
# device_input.click()
# device_input.send_keys('NE5532DR')
# td[4].click()
# time.sleep(2)
# num_input = td[3].find_element_by_tag_name("ti-input")
# time.sleep(4)
#
# time.sleep(2)
#
# while True:
#     kucun = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/table/tbody/tr[1]/td[5]')
#     if kucun.text != "":
#         print(kucun.text)
#         break
# num_input.click()
# num_input.send_keys('1')
#
# # add_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/div[2]/ti-button')
# WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/div[2]/ti-button'))).click()
# add_button.click()

# time.sleep(5)
login_module(driver, name, passwd)
time.sleep(4)
# addcart_module(driver)

# allhandles = driver.window_handles
# for handle in allhandles:
#     driver.switch_to.window(handle)
#     print(driver.current_url)
#
# is_disappeared = WebDriverWait(driver, 60, 0.5, ignored_exceptions=TimeoutException).until(lambda x: x.find_element_by_xpath('find_element_by_xpath').is_displayed())
# Select(driver.find_element_by_xpath('//*[@id="llc-cartpage-ship-to-country"]')).select_by_value('CN')
# jixu_button = driver.find_element_by_xpath('//*[@id="llc-cartpage-ship-to-continue"]')
# jixu_button.click()
# # order_button = driver.find_element_by_xpath('//*[@id="tiCartCalculate_Checkout_top"]')
# # order_button.click()
# is_disappeared = WebDriverWait(driver, 8, 0.5, ignored_exceptions=TimeoutException).until(lambda x: x.find_element_by_xpath('find_element_by_xpath').is_displayed())
# if is_disappeared is False:
#     order_button = driver.find_element_by_xpath('//*[@id="tiCartCalculate_Checkout_top"]')
#     order_button.click()

