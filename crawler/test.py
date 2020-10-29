import time
import random
import json
import requests

def parse_json(s):
    begin = s.find('{')
    end = s.rfind('}') + 1
    return json.loads(s[begin:end])

def check_stock(checksession, skuids, area):
    start_time = int(time.time() * 1000)
    skuidString = ','.join(skuids)
    callback = 'jQuery' + str(random.randint(1000000, 9999999))
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #     "Referer": "https://cart.jd.com/cart.action",
    #     "Connection": "keep-alive",
    #     "Host": "c0.3.cn"
    # }
    #
    url = 'https://c0.3.cn/stocks'
    payload = {
        'type': 'getstocks',
        'skuIds': skuidString,
        'area': area,
        'callback': callback,
        '_': int(time.time() * 1000),
    }
    resp = checksession.get(url=url, params=payload)
    end_time = int(time.time() * 1000)
    print(f"耗时{end_time - start_time}ms")
    print(resp.text)
    inStockSkuid = []
    nohasSkuid = []
    unUseSkuid = []
    for sku_id, info in parse_json(resp.text).items():
        print(sku_id)
        print(info)
        sku_state = info.get('skuState')  # 商品是否上架 0代表下架，1代表上架
        stock_state = info.get('StockState')  # 商品库存状态
        if sku_state == 1 and stock_state in (33, 40):
            inStockSkuid.append(sku_id)
        if sku_state == 0:
            unUseSkuid.append(sku_id)
        if stock_state == 34:
            nohasSkuid.append(sku_id)
    print(f"有货商品{len(inStockSkuid)}")
    print(f"无货商品{len(nohasSkuid)}")
    return inStockSkuid
    # logger.info('检测[%s]个口罩有货，[%s]个口罩无货，[%s]个口罩下柜，耗时[%s]ms', len(inStockSkuid), len(nohasSkuid), len(unUseSkuid),
    #             int(time.time() * 1000) - start)
    #
    # #if len(unUseSkuid) > 0:
    #     logger.info('[%s]口罩已经下柜', ','.join(unUseSkuid))
    # return inStockSkuid

# 本程序用来检查商品是否有货
def send_wx_alert(skuid):
    sc_key = 'SCU121589T7adba0c1839a649182338ed29cfb48275f9a56fa6fcbf'
    text = '商品有货啦：' + skuid
    desp = '[{}](https://item.jd.com/{}.html)'.format(skuid, skuid)
    response = requests.get('https://sc.ftqq.com/{}.send?text={}&desp={}'.format(sc_key, text, desp))

if __name__ == '__main__':
    checksession = requests.session()
    skuid = ['10020498299352', '10022498778136']
    area = '1_2901_4135_0'
    for index in range (1, 2):
        onsale_goods_sku = check_stock(checksession, skuid, area)
        print(onsale_goods_sku)
        for item in onsale_goods_sku:
            send_wx_alert(item)
