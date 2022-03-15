from cmath import atan
from ctypes.wintypes import tagMSG
import enum
import multiprocessing
from posixpath import split
from pip import main
import requests
from bs4 import BeautifulSoup
import firebase as fb
import multiprocessing

STORE = 'store'
TITLE = 'title'
THUMBNAIL = 'thumbnail'
URL = 'url'
FMKOREA = 'fmkorea'
EOMISAE = 'emoisae'
datas = []

# 제목 / url / 썸네일만 가져오기!
urlList = ['https://www.fmkorea.com/index.php?mid=hotdeal&category=1196845284',
            'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=12',
            'https://eomisae.co.kr/os']

def fmKorea():
    host = 'https://www.fmkorea.com'
    response = requests.get(urlList[0])
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # select 정의하기
        itemLists = soup.select('li.li.li_best2_pop0')
        for item in itemLists:
            # 썸네일 가져오기
            imgTag = item.find('img')
            thumbnail = ""
            if imgTag != None:
                thumbnailUrl = 'https:' + imgTag.attrs['data-original']
                thumbnail = thumbnailUrl
            # 제목 가져오기
            titleTag = item.find('h3')
            title = titleTag.text.split('[')[0].strip()
            itemLink = host + titleTag.find('a').attrs['href']
            data = {STORE : FMKOREA,
                    TITLE : title,
                    THUMBNAIL : thumbnail,
                    URL : itemLink}
            datas.append(data)
    else:
        print(response.status_code)

# def ppomppu():
#     response = requests.get(urlList[1])
#     if response.status_code == 200:
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')

#         itemLists = soup.findAll('tr', {'class': ['list0', 'list1']})
#         for idx, itemList in enumerate(itemLists, 1):
#             tableTag = itemList.find('table')
#             aTag = tableTag.find('a')
#             url = 'https://www.ppomppu.co.kr/zboard/' + aTag.attrs['href']
#             urls.append(url)
#             imgTag = aTag.find('img')
#             thumbnailUrl = 'https:' + imgTag.attrs['src']
#             thumbnails.append(thumbnailUrl)
#             # 글번호 숫자인 것만가져오기
#             title = tableTag.find('font').text.strip()
#             titles.append(title)
#     else:
#         print(response.status_code)

def eomisae():
    response = requests.get(urlList[2])
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        thumbnails = []
        titles = []
        urls = []

        itemLists = soup.select('div.card_el.n_ntc.clear')
        for item in itemLists:
            tmb = item.find('img', {'class': 'tmb'}).attrs['src']
            thumbnail = ''
            if 'crop' in tmb:
                thumbnail = tmb
            aTag = item.find('a', {'class' : 'pjax'})
            url = aTag.attrs['href']
            title = aTag.text
            data = {STORE : EOMISAE,
                    TITLE : title,
                    THUMBNAIL : thumbnail,
                    URL : url}
            datas.append(data)
    else:
        print(response.status_code)
            
def main():
    # p1 = multiprocessing.Process(target=fmKorea)
    # p2 = multiprocessing.Process(target=eomisae)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    fmKorea()
    eomisae()

if __name__ == "__main__":
    main()
    fb.setup()
    for i in range(0, len(datas)):
        fb.update(datas[i])
else:
    print("임포트")
    main()