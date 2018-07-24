import requests
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"


def get_captcha(url):
    html = getHtmlText(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    # 找到验证码图片所在列表
    web_list = soup.find('div', class_='portal-login part')
    web = web_list.find_all('div', class_='form-group')
    for top in web:
        img_url = top.find('img')
        if img_url:
            # 爬取200张验证码
            for name in range(200):
                with open(r'D:\system 文件\Desktop\img\img' + str(name) + '.png', 'wb') as f:
                    f.write(requests.get("https://open.iot.10086.cn" + img_url.get('src')).content)


def main():
    url = 'https://open.iot.10086.cn/login?'
    get_captcha(url)


if __name__ == "__main__":
    main()