import requests
from bs4 import BeautifulSoup
import csv


def download(url):
    '''
    下载模块
    '''
    headers = {}
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    return response.text


def get_content_first_page(html, year):
    '''
    数据采集模块

    获取排名在1-100的公司列表，且包含表头
    '''
    soup = BeautifulSoup(html, "lxml")
    body = soup.body
    body_content = body.find('div', {'id': 'bodyContent'})
    tables = body_content.find_all('table', {'class': 'XXXXtable'})

    # tables 一共有3个， 最后一个才是我们想要的
    trs = tables[-1].find_all('tr')
