import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent



def login(name, passwd):
    # url = 'https://pan.baidu.com/'
    url = 'https://www.ti.com.cn/'
    # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    # s = Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    chrome_driver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument(f'user-agent={userAgent}')
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    script = '''
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    '''
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
    with open('stealth.min.js') as f:
        js = f.read()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
    # driver = webdriver.Chrome(service=s)
    # driver.maximize_window()
    # driver.get(url)
    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)
    driver.implicitly_wait(3)
    print('开始登录')
    # chg_field = driver.find_element_by_class_name('pass-login-tab').find_element_by_class_name('account-title')
    # chg_field.click()

    # container = driver.find_element_by_id('login-container')
    # name_field = driver.find_element_by_css_selector("#TANGRAM__PSP_4__userName")
    # # driver.find_element_by_id('TANGRAM__PSP_4__userName')
    # name_field.send_keys(name)
    # passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    # passwd_field.send_keys(passwd)
    # login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
    # login_button.click()
    # time.sleep(20)
    # return driver.get_cookies()

    ti_login = driver.find_element_by_xpath('//*[@id="tiResponsiveHeader"]/div/div[2]/div[2]/div[1]/ti-login')
    ti_login.click()
    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)
    driver.implicitly_wait(2)

    # ti登陆
    # userName = driver.find_element_by_name('username')
    # userName.send_keys(name)
    # time.sleep(3)
    # next_button = driver.find_element_by_id('nextbutton')
    # next_button.click()
    # password = driver.find_elements_by_name('password')
    #
    # password[1].send_keys(passwd)
    # time.sleep(3)
    # login_button = driver.find_element_by_name('loginbutton')
    # time.sleep(3)
    # login_button.click()
    #
    # allhandles = driver.window_handles
    # for handle in allhandles:
    #     driver.switch_to.window(handle)
    #     print(driver.current_url)
    # driver.implicitly_wait(3)
    cart = driver.find_element_by_link_text("快速添加到购物车")
    # cart = a_href[0]
    # for i in a_href:
    #     if i.get_attribute("href") == "https://www.ti.com.cn/zh-cn/ordering-resources/buying-tools/quick-add-to-cart.html":
    #         cart = i
    #         break
    cart.click()

    allhandles = driver.window_handles
    for handle in allhandles:
        driver.switch_to.window(handle)
        print(driver.current_url)
    driver.implicitly_wait(2)
    table = driver.find_elements_by_tag_name("table")
    print(len(table))
    throws = table[0].find_elements_by_tag_name("tr")
    print(len(throws))
    td = throws[1].find_elements_by_tag_name("td")
    print(len(td))
    device_input = td[1].find_element_by_tag_name("ti-input")
    # print(len(device_input))
    device_input.click()
    device_input.send_keys('NE5532DR')
    td[4].click()
    time.sleep(2)
    num_input = td[3].find_element_by_tag_name("ti-input")
    time.sleep(4)
    num_input.click()
    num_input.send_keys('5')
    time.sleep(2)
    add_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/div[2]/ti-button')
    add_button.click()

    # cart.click()
    time.sleep(15)

    return driver.get_cookies()


if __name__ == '__main__':
    name = '893866506@qq.com'
    passwd = 'Zxlzxl123'
    # name = '641896601@qq.com'
    # passwd = 'Zwylisy33'
    cookies = login(name, passwd)
    print(cookies)

    # # url = 'https://pan.baidu.com/'
    # url = 'https://login.ti.com/as/authorization.oauth2?response_type=code&scope=openid%20email%20profile&client_id=DCIT_ALL_WWW-PROD&state=rC42ffNfSRC14JjID87XMOVT27k&redirect_uri=https%3A%2F%2Fwww.ti.com.cn%2Foidc%2Fredirect_uri%2F&nonce=4m-pGNIwl0mUYSDIsb7lVvUgD4Si7DyweQJPup7_Jq4&response_mode=form_post'
    # # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    # s = Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    # driver.maximize_window()
    # driver.get(url)
    # driver.implicitly_wait(3)
    # print('开始登录')
    # # chg_field = driver.find_element_by_class_name('pass-login-tab').find_element_by_class_name('account-title')
    # # chg_field.click()
    #
    # # container = driver.find_element_by_id('login-container')
    # # name_field = driver.find_element_by_css_selector("#TANGRAM__PSP_4__userName")
    # # # driver.find_element_by_id('TANGRAM__PSP_4__userName')
    # # name_field.send_keys(name)
    # # passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    # # passwd_field.send_keys(passwd)
    # # login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
    # # login_button.click()
    # # time.sleep(20)
    # # return driver.get_cookies()
    #
    # # ti登陆
    # userName = driver.find_element_by_name('username')
    # userName.send_keys(name)
    # time.sleep(1)
    # next_button = driver.find_element_by_id('nextbutton')
    # next_button.click()
    # password = driver.find_elements_by_name('password')
    #
    # password[1].send_keys(passwd)
    # time.sleep(1)
    # login_button = driver.find_element_by_name('loginbutton')
    # time.sleep(1)
    # login_button.click()
    # # login_button.send_keys(Keys.ENTER)
    # # driver.implicitly_wait(10)
    # allhandles = driver.window_handles
    # for handle in allhandles:
    #     driver.switch_to.window(handle)
    #     print(driver.current_url)
    # driver.implicitly_wait(3)
    # cart = driver.find_element_by_link_text("快速添加到购物车")
    # # cart = a_href[0]
    # # for i in a_href:
    # #     if i.get_attribute("href") == "https://www.ti.com.cn/zh-cn/ordering-resources/buying-tools/quick-add-to-cart.html":
    # #         cart = i
    # #         break
    # cart.click()
    #
    # allhandles = driver.window_handles
    # for handle in allhandles:
    #     driver.switch_to.window(handle)
    #     print(driver.current_url)
    # driver.implicitly_wait(2)
    # table = driver.find_elements_by_tag_name("table")
    # print(len(table))
    # throws = table[0].find_elements_by_tag_name("tr")
    # print(len(throws))
    # td = throws[1].find_elements_by_tag_name("td")
    # print(len(td))
    # device_input = td[1].find_element_by_tag_name("ti-input")
    # # print(len(device_input))
    # device_input.click()
    # device_input.send_keys('DLP4500NIRAFQD')
    # num_input = td[3].find_element_by_tag_name("ti-input")
    # num_input.click()
    # num_input.send_keys('5')
    #
    # add_button = driver.find_element_by_xpath(
    #     '/html/body/div[2]/div[2]/div/div/div/div[2]/div/ti-quick-add-to-cart/div/div/div[2]/ti-button')
    # add_button.click()
    #
    # # cart.click()
    # time.sleep(15)
