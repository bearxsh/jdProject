
# 第二步：重用第一步的Chrome和环境，实现自动下单锁定
from ReuseChrome import ReuseChrome
from selenium.webdriver.support.ui import WebDriverWait
import logging
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from selenium.webdriver.common.keys import Keys
from time import sleep

# executor和session_id为第一步生成的url和session_id
# executor = "http://127.0.0.1:54298"
# session_id = "3969e9f43415e21498d5c07510f21b69"
# driver = ReuseChrome(command_executor=executor, session_id=session_id)

# newWindow = 'window.open("https://www.jd.com")'
# driver.execute_script(newWindow)
# all_windows = driver.window_handles
# print(len(all_windows))
# driver.switch_to.window(all_windows[len(all_windows) - 1])
# searchInput = driver.find_element_by_xpath('//*[@id="kw"]')
# searchInput.send_keys('Trump')
# searchInput.send_keys(Keys.RETURN)
#
# newWindow = 'window.open("https://www.baidu.com")'
# driver.execute_script(newWindow)
# all_windows = driver.window_handles
# print(len(all_windows))
# driver.switch_to.window(all_windows[len(all_windows) - 1])
# searchInput = driver.find_element_by_xpath('//*[@id="kw"]')
# searchInput.send_keys('Trump')
# searchInput.send_keys(Keys.RETURN)


# def tab_job(dri, all_win, ind):
#     #print(driver)
#     print(ind)
#     #sleep(3)
#     dri.switch_to.window(all_win[ind])
#     dri.refresh()
#     # search = driver.find_element_by_xpath('//*[@id="key"]')
#     # search.clear()
#     # search.send_keys('排位')
#     #dri.refresh()


if __name__ == '__main__':
    executor = "http://127.0.0.1:60534"
    session_id = "78a33f8f1cc0632a87e8e961246e442f"
    driver = ReuseChrome(command_executor=executor, session_id=session_id)
    wait = WebDriverWait(driver, 5, 0.1)
    all_windows = driver.window_handles
    num = len(all_windows)
    print(num)
    print('------')
    # pool = Pool(processes=num)
    for index in range(0, num):
        #pool.apply_async(tab_job, args=(driver, all_windows, index,))
        print(index)
        driver.switch_to.window(all_windows[index])
        #driver.refresh()
        try:
            reserveBtn = driver.find_element_by_xpath('//*[@id="btn-reservation"]')
            # 判断支付定金按钮是否可以点击，如果不可点击说明没货，跳过此次循环
            disable = "btn-disable" in reserveBtn.get_attribute("class")
            if disable:
                continue
            reserveBtn.click()
            wait.until(lambda x: x.find_element_by_xpath('//*[@id="presaleEarnest"]'))
            confirmBtn = driver.find_element_by_xpath('//*[@id="presaleEarnest"]')
            confirmBtn.click()
        except Exception as e:
            logging.exception(e)

