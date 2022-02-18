import requests
from bs4 import BeautifulSoup

urlList = ['https://www.fmkorea.com/index.php?mid=hotdeal&category=1196845284',
            'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=12',
            'https://eomisae.co.kr/os']

def fmKorea():
    response = requests.get(urlList[0])
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # select 정의하기
        title_elem = soup.select('li.li.li_best2_pop0 > div.li > h3.title > a.hotdeal_var8')
        dealInfo_elem = soup.select('li.li.li_best2_pop0 > div.li > div.hotdeal_info')
        count = len(title_elem)
        # 제목 가져오기
        titles = []
        for title in title_elem:
            text = title.text.split('[')[0]
            titles.append(text.strip())
        # 핫딜 정보 가져오기
        dealInfos = []
        for deal in dealInfo_elem:
            dealInfo = deal.text.split('/')
            mall = dealInfo[0].strip().split(':')[1].strip()
            itemPrice = dealInfo[1].strip().split(':')[1].strip()
            shipPrice = dealInfo[2].strip().split(':')[1].strip()
            dealInfos.append((mall, itemPrice, shipPrice))
        for i in range(0, count):
            #print(titles[i], dealInfos[i])
            titles
    else:
        print(response.status_code)

def ppomppu():
    response = requests.get(urlList[1])
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        dealInfos_elem = soup.select('div > a > font.list_title')
        dealInfos = []
        for dealInfo in dealInfos_elem:
            print(dealInfo.text)

fmKorea()
ppomppu()