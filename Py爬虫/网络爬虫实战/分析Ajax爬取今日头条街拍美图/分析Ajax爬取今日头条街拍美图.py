import requests
from urllib.parse import urlencode
import time


# 实现方法get_page()来加载单个Ajax请求的结果。传入会变化的参数
def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': time.time()
    }

    url = 'http://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        raise None


# 实现一个解析方法：提取每条数据的image_list字段中的每一张图片链接，将图片链接和图片所属的标题一并返回，此时可以构造一个生成器。
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            try:  # 如果不存在执行continue
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }
            except Exception:
                continue


# 接下来实现一个保存图片的方法save_image()，其中item就是前面get_images()方法返回的一个字典。
# 在该方法中，首先根据item的title来创建文件夹，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写入文件。
# 图片的名称可以使用其内容的MD5值，这样可以去除重复
import os
from hashlib import md5


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


# 最后，只需要构造一个offset数组，遍历offset，提取图片链接，将其下载
from multiprocessing.pool import Pool


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        try:  # 如果不存在就执行continue
            print(item)
            save_image(item)
        except Exception as e:
            continue


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
