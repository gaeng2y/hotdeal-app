import requests
from bs4 import BeautifulSoup

urlList = ['https://www.fmkorea.com/index.php?mid=hotdeal&category=1196845284',
            'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&category=12',
            'https://eomisae.co.kr/os']

'''
for url in urlList:
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
    else:
        print(response.status_code)
        '''
response = requests.get(urlList[0])
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
else:
    print(response.status_code)
