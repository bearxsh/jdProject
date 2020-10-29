import requests

if __name__ == '__main__':
    sc_key = 'SCU121589T7adba0c1839a649182338ed29cfb48275f9a56fa6fcbf'
    text = '北京欢迎你'
    desp = '设计师'
    response = requests.get('https://sc.ftqq.com/{}.send?text={}&desp={}'.format(sc_key, text, desp))
    print(response)
