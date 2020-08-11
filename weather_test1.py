# 引入request、json模块
# import requests
import json
import urllib.request
from urllib.parse import urlencode
# import itchat


def weather_main():
    # 输入城市名称
    city = input('请输入要查询的城市名称： ')
    # 定义城市参数
    location = city

    # 拼接输入和key
    params_weather = {
        'location': location,
        'key': 'dcb2ae571d2a47c8bbc18930513b170b'
    }

    weather_base_url = 'https://free-api.heweather.net/s6/weather/now?'
    air_base_url = 'https://free-api.heweather.net/s6/air/now?'
    life_base_url = 'https://free-api.heweather.net/s6/weather/lifestyle?'
    today_base_url = 'https://free-api.heweather.net/s6/weather/forecast?'
    url1 = weather_base_url + urlencode(params_weather)
    url2 = air_base_url + urlencode(params_weather)
    url3 = life_base_url + urlencode(params_weather)
    url4 = today_base_url + urlencode(params_weather)

    # 打印拼接地址
    # print(url1)
    # print(url2)
    # print(url3)
    # print(url4)

    # 使用request发起请求，接受返回的结果
    req_weather = urllib.request.urlopen(url1)
    req_air = urllib.request.urlopen(url2)
    req_life = urllib.request.urlopen(url3)
    req_today = urllib.request.urlopen(url4)
    resp_weather = req_weather.read().decode('utf-8')
    resp_air = req_air.read().decode('utf-8')
    resp_life = req_life.read().decode('utf-8')
    resp_today = req_today.read().decode('utf-8')
    # print(resp_weather)
    # print(resp_air)
    # print(resp_life)
    # print(resp_today)

    # 将json转化为python的数据结构
    json_date_air = json.loads(resp_air)
    json_date_weather = json.loads(resp_weather)
    json_date_life = json.loads(resp_life)
    json_date_today = json.loads(resp_today)
    date_air = json_date_air['HeWeather6'][0]
    date_weather = json_date_weather['HeWeather6'][0]
    date_life = json_date_life['HeWeather6'][0]
    date_today = json_date_today['HeWeather6'][0]

    # 获取pm2.5的数值
    pm25 = date_air['air_now_city']['pm25']

    # 获取空气质量
    # air_qlty = date_air['air_now_city']['qlty']

    # 获取城市
    city = date_weather['basic']['location']

    # 获取现在的天气、温度、体感温度、风向、风力等级
    now_weather = date_weather['now']['cond_txt']  # 天气描述
    now_tmp = date_weather['now']['tmp']  # 温度
    # now_fl = date_weather['now']['fl']  # 体感温度
    # now_wind_dir = date_weather['now']['wind_dir']  # 风向
    now_wind_sc = date_weather['now']['wind_sc']  # 风力

    # 今天的天气，读取第1个json列表内容，并输出
    today = date_today['daily_forecast'][0]
    today_weather_day = today['cond_txt_d']
    today_weather_night = today['cond_txt_d']
    today_weather_max = today['tmp_max']
    today_weather_min = today['tmp_min']
    today_weather_dir = today['wind_dir']
    today_weather_sc = today['wind_sc']

    # 天气建议
    # 舒适度，读取第1个json列表内容，并输出
    comf_comf = date_life['lifestyle'][0]
    comf = comf_comf['brf']
    comf_txt = comf_comf['txt']

    # 穿衣说明，读取第2个json列表内容，并输出
    comf_drsg = date_life['lifestyle'][1]
    drsg = comf_drsg['brf']
    drsg_txt = comf_drsg['txt']

    # 流感指数
    comf_flu = date_life['lifestyle'][2]
    flu = comf_flu['brf']
    flu_txt = comf_flu['txt']

    # 输出以上内容的详细内容
    # print(pm25)
    # print(air_qlty)
    # print(city)
    # print(now_weather)
    # print(now_tmp)
    # print(now_fl)
    # print(now_wind_dir)
    # print(now_wind_sc)
    # print(today_weather_day)
    # print(today_weather_night)
    # print(today_weather_max)
    # print(today_weather_min)
    # print(today_weather_dir)
    # print(today_weather_sc)

    weather_forcast_txt = [
        "%s今天白天天气%s，夜间天气%s，最高气温%s摄氏度，最低气温%s摄氏度，风力%s，风向%s，天气舒适度：%s，%s流感指数：%s，%s穿衣指数：%s，%s现在外面的天气：%s，当前温度：%s，当前风力：%s"
        "，当前PM指数：%s "
        % (city,
           today_weather_day,
           today_weather_night,
           today_weather_max,
           today_weather_min,
           today_weather_sc,
           today_weather_dir,
           comf,
           comf_txt,
           flu,
           flu_txt,
           drsg,
           drsg_txt,
           now_weather,
           now_tmp,
           now_wind_sc,
           pm25
           )]
    print(weather_forcast_txt)

    # nickname = input('please input your firends\' nickname: ')
    # users = itchat.search_friends(name = nickname)
    # print(users)
    # userName = users[0]['UserName']
    # itchat.send(weather_forcast_txt, toUserName=userName)

    # print('succeed')


weather_main()
