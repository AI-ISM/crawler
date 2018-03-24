from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import random
import datetime


# def getLinks(url):
#     try:
#         html = urlopen('https://en.wikipedia.org'+url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(), 'html5lib')
#         # title = bsObj.find_all({'span'}, {"class": {"green"}})
#         # title = bsObj.find("table", {'id': 'giftList'}).children
#         # title = bsObj.find("table", {'id': 'giftList'}).next_siblings
#         # title = bsObj.find_all('a')
#         links = bsObj.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#     except AttributeError as e:
#         return None
#     return links
#
#
# random.seed(datetime.datetime.now())
# pages = set()
# links = getLinks("/wiki/Eric_Idle")
# if links is None:
#     print("Title not found")
# else:
#     while len(links) > 0:
#         globals(pages)
#         newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#         print(newArticle)
#         links = getLinks(newArticle)

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html, 'html5lib')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").find_all('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面缺少一些属性！不过不用担心！')

    for link in bsObj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新页面
                newPage = link.attrs['href']
                print('-----\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

