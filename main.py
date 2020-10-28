
# 第二步：重用第一步的Chrome和环境，实现自动下单锁定
from ReuseChrome import ReuseChrome
from selenium.webdriver.support.ui import WebDriverWait
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
        reserveBtn = driver.find_element_by_xpath('//*[@id="btn-reservation"]')
        reserveBtn.click()
        wait.until(lambda x: x.find_element_by_xpath('//*[@id="presaleEarnest"]'))
        confirmBtn = driver.find_element_by_xpath('//*[@id="presaleEarnest"]')
        confirmBtn.click()
        # search = driver.find_element_by_xpath('//*[@id="key"]')
        # search.clear()
        # search.send_keys('排位')
        # search.send_keys(Keys.RETURN)

    # pool.close()
    # pool.join()

# print(len(all_windows))
# with ThreadPoolExecutor(max_workers=7) as t:
#     t.submit(tab_job(0))
#     t.submit(tab_job(1))
#     t.submit(tab_job(2))
#     t.submit(tab_job(3))
#     t.submit(tab_job(4))
#     t.submit(tab_job(5))
#     t.submit(tab_job(6))
# for index in range(0, len(all_windows)):

# t.submit(tab_job, index)
# searchInput = driver.find_element_by_xpath('//*[@id="InitCartUrl"]')
# searchInput.click()
# searchInput.clear()
# searchInput.send_keys('阿迪')
# searchInput.send_keys(Keys.RETURN)
# sleep(2)

# driver.switch_to.window(all_windows[5])
# searchInput = driver.find_element_by_xpath('//*[@id="kw"]')
# searchInput.clear()
# searchInput.send_keys('delete')
# searchInput.send_keys(Keys.RETURN)
