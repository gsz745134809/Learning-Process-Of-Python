from datetime import datetime
from urllib.parse import urlencode
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import pymongo
from zhilian_kw_config import *
import time
from itertools import product

client = pymongo.MongoClient(host=MONGO_URI, port=PORT)
db = client[MONGO_DB]


def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Cookie': 'sts_deviceid=16a02a72b2a1f7-0c989c290e9631-9333061-1327104-16a02a72b2c49b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a02a73507151-0a3f50656e9988-9333061-1327104-16a02a735087f4%22%2C%22%24device_id%22%3A%2216a02a73507151-0a3f50656e9988-9333061-1327104-16a02a735087f4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; ZP_OLD_FLAG=false; LastCity=%E5%B9%BF%E5%B7%9E; LastCity%5Fid=763; dywez=95841923.1554822801.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; __utmz=269921210.1554822801.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); smidV2=20190409231321087a75c916ab1655a5fc0e8ba21d8b2d00dc56f0f9dd57120; dywea=95841923.1387319876715970600.1554822801.1554822801.1554864277.2; dywec=95841923; __utma=269921210.1497482125.1554822801.1554822801.1554864277.2; __utmc=269921210; __utmt=1; acw_tc=2760828415548642838407830efd3be1dc98c1f88f8cb5ea4d5650b415e3c5; jobRiskWarning=true; sts_sg=1; sts_sid=16a05222f43a76-00c7453fa03575-9333061-1327104-16a05222f44a1f; sts_chnlsid=Unknown; zp_src_url=http%3A%2F%2Fforbidden.zhaopin.com%2Ferror_ip.html%3Fip%3D220.115.183.143; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1554822674,1554864288; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; campusOperateJobUserInfo=4f9169be-500a-42cc-9345-c8e710331d12; referrerUrl=https%3A//www.zhaopin.com/; dyweb=95841923.14.6.1554864443298; __utmb=269921210.14.6.1554864443301; sts_evtseq=6; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1554864482; stayTimeCookie=1554864482012',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0'}
    response = requests.get(url, headers=headers)
    return response.text


def get_content(html):
    # 记录保存日期
    date = datetime.now().date()
    date = datetime.strftime(date, '%Y-%m-%d')  # 转变成str

    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find('div', {'class': 'newlist_list_content'})

    if data_main:
        tables = data_main.find_all('table')

        for i, table_info in enumerate(tables):
            if i == 0:
                continue
            tds = table_info.find('tr').find_all('td')
            zwmc = tds[0].find('a').get_text()  # 职位名称
            zw_link = tds[0].find('a').get('href')  # 职位链接
            fkl = tds[1].find('span').get_text()  # 反馈率
            gsmc = tds[2].find('a').get_text()  # 公司名称
            zwyx = tds[3].get_text()  # 职位月薪
            gzdd = tds[4].get_text()  # 工作地点
            gbsj = tds[5].find('span').get_text()  # 发布日期

            tr_brief = table_info, find('tr', {'class': 'newlist_tr_detail'})  # 招聘简介

            brief = tr_brief.find('li', {'class': 'newlist_detail_last'}).get_text()

            # 用生成器获取信息
            yield {
                'zwmc': zwmc,  # 职位名称
                'fkl': fkl,  # 反馈率
                'gsmc': gsmc,  # 公司名称
                'zwyx': zwyx,  # 职位月薪
                'gzdd': gzdd,  # 工作地点
                'gbsj': gbsj,  # 公布时间
                'brief': brief,  # 招聘简介
                'zw_link': zw_link,  # 网页链接
                'save_date': date  # 记录信息保存的日期

            }


def main(args):
    basic_url = 'https://xiaoyuan.zhaopin.com/full/0/0_0_0_0_0_-1_'
    added_url = '_1_0'

    for keyword in KEYWORDS:
        mongo_table = db[keyword]
        paras = {
            'jl': args[0],
            'kw': keyword,
            'p': args[1]  # 第X页
        }
        url = basic_url + urlencode(paras) + added_url
        print(url)
        html = download(url)
        time.sleep(0.5)
        # print(html)
        if html:
            data = get_content(html)
            for item in data:
                if mongo_table.insert({'zw_link': item['zw_link']}, {'$set': item}):
                    print('已保存记录：', item)


if __name__ == '__main__':
    start = time.time()
    number_list = list(range(TOTAL_PAGE_NUMBER))
    args = product(ADDRESS, number_list)
    pool = Pool()
    pool.map(main, args)  # 多进程运行
    end = time.time()
    print('Finished, task runs %s seconds.' % (end - start))
