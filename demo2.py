# http://www.521609.com/meinvxiaohua/

import requests
from bs4 import BeautifulSoup
from os import path
import os # os 安装
import shutil # OS实现
import threading # 多线程
import time # 自己决定

# 观察入口页面
# http://www.521609.com/meinvxiaohua/  入口url
# User-Agent:

# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

headers = {
    'Referer': 'http://www.521609.com/meinvxiaohua/',
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 '
}

# 获取首页源代码 通用型获取
def get_html(url):
    try:
        # 请求交互--->获取源代码
        response = requests.get(url, headers)  # b 不要忘记
        response.encoding = 'gb2312'
        return response.text  # 区别
    except Exception as e:
        print(e)

# 保存数据 存放指定目录 设计
def create_dir():       # 存放数据资源   les2 目录名称---> 创建新的目录(假设目录名称show) 存在怎么样？如果不存在有怎么样
    # 判断show目录不存在？  小知识点
    if path.exists('./show/'):  # 满足
        shutil.rmtree('./show/')
        print('目录存在,先删除')
    # 不存在则创建
    os.mkdir('./show/')
    print('创建新的目录')

# 子标签下最大页面数----> 11页
def get_max_page():
    url = 'http://www.521609.com/meinvxiaohua/' # -->获取入口也没源代码-->解析最大页面
    html = get_html(url) # html-->源代码--->解析数据(不是图片数据，而是最大页数)
    # 包装 soup-->为什么要包装--->更方便获取数据
    soup = BeautifulSoup(html, 'lxml') # 第二个参数：解析方式 高效 html xml(轻量级数据交换)
    # 获取最大页数    怎么获取11？ strong 标签中  .text
    pages = soup.find('div', class_= 'listpage').find_all('li')[-1].find('strong').text # 字符串形式
    return int(pages)

# 下载每一页图片
def down_show(html, page):
    try:
        soup = BeautifulSoup(html, 'lxml')
        all_img = soup.find('div', class_='index_img').find_all('img')
        #
        num = 1 # 1（起始页数）,2,3...    第几张图片
        for img in all_img:
            src = img.get('src')    # 直接请求？ 不能直接请求
            url = 'http://www.521609.com'+ src
            with open('show/' + '%s页-%s.jpg' % (page, num), 'wb') as file:
                file.write(requests.get(url=url, headers=headers).content)
            num += 1
    except Exception as e:
        print(e)


# 观察-->再观察
# 下载11页数
def get_pages(max_page):
    # 前面的规律 120--->     ？   固定部分    120
    start = '120'
    for index in range(1, max_page + 1):    # 120   1,2,3,4,5,6……11(这个部分)
        # 关键部分 120 + 10 = 130 1210
        if index < 10:      # 10, 11
            page = str(int(start) + index)
        else:
            page = str(int(start)//10) + str(index)  # '12' + '11'      '1211'
        url = 'http://www.521609.com/meinvxiaohua/list%s.html' % page
        html = get_html(url)
        thread = threading.Thread(target='down_show', args=(html,page))  # 元\组
        thread.start()
    print('美女图片爬取完毕')

def main(page):
    create_dir()
    get_pages(page)

if __name__=='__main__':
    max_page = get_max_page()
    main(max_page)