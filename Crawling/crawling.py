from cmath import atan
import enum
from posixpath import split
import requests
from bs4 import BeautifulSoup

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

        thumbnails = []
        titles = []
        mall = []
        itemPrices = []
        shippingPrices = []
        urls = []

        for item in itemLists:
            # 썸네일 가져오기
            imgTag = item.find('img')
            if imgTag != None:
                thumbnailUrl = 'https:' + imgTag.attrs['data-original']
                thumbnails.append(thumbnailUrl)
            else:
                thumbnails.append("")
            # 제목 가져오기
            titleTag = item.find('h3')
            title = titleTag.text.split('[')[0].strip()
            titles.append(title)
            itemLink = host + titleTag.find('a').attrs['href']
            urls.append(itemLink)
            # 쇼핑몰/가격/배송비
            infoTag = item.select('div.hotdeal_info > span')
            infos = []
            for info in infoTag:
                detailInfo = info.text.strip().split(':')[1].strip()
                infos.append(detailInfo)
            mall.append(infos[0])
            itemPrices.append(infos[1])
            shippingPrices.append(infos[2])
    else:
        print(response.status_code)

def ppomppu():
    response = requests.get(urlList[1])
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        itemLists = soup.findAll('tr', {'class': ['list0', 'list1']})
        for idx, itemList in enumerate(itemLists, 1):
            tableTag = itemList.find('table')
            aTag = tableTag.find('a')
            url = 'https://www.ppomppu.co.kr/zboard/' + aTag.attrs['href']
            imgTag = aTag.find('img')
            thumbnailUrl = 'https:' + imgTag.attrs['src']
            #print(url)
            #print(thumbnailUrl)
            # 글번호 숫자인 것만가져오기
            dealInfo = (tableTag.find('font').text)
            splitDealInfo = dealInfo.split(']')
            mall = ""
            if splitDealInfo[0][0] == '[':
                mall = splitDealInfo[0][1:]
            print(mall)
            #print(splitDealInfo)
            
#fmKorea()
ppomppu()