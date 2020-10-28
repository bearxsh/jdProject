# 第二步：重用第一步的Chrome及其环境，实现自动下单锁定
from ReuseChrome import ReuseChrome
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time


def get_num_by_goods_title(goods_title):
    # 型号及其数量
    goods_category_num_dict = {'ABAP129': 3,
                               }
    goods_num = 1
    for key in goods_category_num_dict.keys():
        if key in goods_title:
            goods_num = goods_category_num_dict[key]
            break
    return goods_num


if __name__ == '__main__':
    executor = "http://127.0.0.1:60534"
    session_id = "78a33f8f1cc0632a87e8e961246e442f"
    driver = ReuseChrome(command_executor=executor, session_id=session_id)
    wait = WebDriverWait(driver, 5, 0.1)
    all_windows = driver.window_handles
    tab_num = len(all_windows)
    print('------------------------')
    print(f"当前激活的Tab页数量：{tab_num}")
    print('------------------------')
    start_time = time.time()

    for index in range(0, tab_num):
        print(index)
        driver.switch_to.window(all_windows[index])
        try:
            reserveBtn = driver.find_element_by_xpath('//*[@id="btn-reservation"]')
            # 判断支付定金按钮是否可以点击，如果不可点击说明没货，跳过此次循环
            disable = "btn-disable" in reserveBtn.get_attribute("class")
            if disable:
                continue
            title = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[1]').text
            print(title)
            num = get_num_by_goods_title(title)
            print(f"应当购买的数量：{num}")
            num_input = driver.find_element_by_xpath('//*[@id="buy-num"]')
            num_input.clear()
            num_input.send_keys(num)

            reserveBtn.click()
            # 这一步必须有，否者会报错：找不到该元素
            wait.until(lambda x: x.find_element_by_xpath('//*[@id="presaleEarnest"]'))
            confirmBtn = driver.find_element_by_xpath('//*[@id="presaleEarnest"]')
            confirmBtn.click()
        except Exception as e:
            logging.exception(e)

    end_time = time.time()
    use_time = end_time - start_time
    print(f"总共耗时：{use_time}")
