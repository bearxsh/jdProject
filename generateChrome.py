# 第一步：生成url和session_id，并登录京东
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    browser = webdriver.Chrome('D:\Application\chromedriver_win32\chromedriver.exe')
    browser.get('https://item.jd.com/10022224775744.html')
    print(browser.command_executor._url)
    print(browser.session_id)
