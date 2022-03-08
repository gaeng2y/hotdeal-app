from cmath import atan
import enum
from posixpath import split
from pip import main
import requests
from bs4 import BeautifulSoup

thumbnails = []
titles = []
urls = []

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
            urls.append(url)
            imgTag = aTag.find('img')
            thumbnailUrl = 'https:' + imgTag.attrs['src']
            thumbnails.append(thumbnailUrl)
            # 글번호 숫자인 것만가져오기
            title = tableTag.find('font').text.strip()
            titles.append(title)
    else:
        print(response.status_code)

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
            if 'crop' in tmb:
                thumbnails.append(tmb)
            else:
                thumbnails.append('')
            aTag = item.find('a', {'class' : 'pjax'})
            url = aTag.attrs['href']
            urls.append(url)
            title = aTag.text
            titles.append(title)
    else:
        print(response.status_code)
            
def main():
    fmKorea()
    ppomppu()
    eomisae()

if __name__ == "__main__":
    main()
    print(thumbnails, titles, urls)
else:
    print("임포트")
    main()