# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
#
# greet_user()

# def greet_user(username):
#     """显示简单的问候语"""
#     print("Hello, " + username.title() + "!")
#
# greet_user('jesse')

# 8.1case
# 编写一个名为display_message()的函数
# 打印一个句子，指出你在本章学的是什么
# def display_message():
#     """显示本章学的内容"""
#     print("本章学习了函数的设置")
# display_message()

# 8.2case
# 编写一个名为favorite_book的函数，其中包含一个名为title的形参
# 这个函数打印一条消息
# def favorite_book(title):
#     """显示书籍的名字"""
#     print("One of my favorite books is " + title.title() + ".")
# favorite_book('alice in wonderland')

# 8.3.4 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     """返回简洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# # 这是一个无限循环！
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("Frist name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# 变成可结束的方式
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# 8.4 传递列表
def greet_user(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)


# 8-6 城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串
# "Santiago, Chile"
# def city_country(city_name, country_name):
#     country = city_name + ',' + country_name
#     return country.title()
#
# nation = city_country('beijing', 'china')
# print(nation)
#
# nation = city_country('tokyo', 'japan')
# print(nation)
#
# nation = city_country('new york', 'america')
# print(nation)

# 8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回值，以核实字典正确地存储了专辑的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时制定了歌曲数，就将这个值添加到表示专辑的字典中。
# 调用这个函数，并至少一次调用中指定专辑包含的歌曲数。
# def make_album(artist_name, album_name, number=''):
#     musician_information = {'artist': artist_name, 'album': album_name,}
#     if number:
#         musician_information['number'] = number
#     return musician_information
#
# information = make_album('jimi', 'No.7', number=7)
# print(information)
#
# information = make_album('franz', 'No.8')
# print(information)
#
# information = make_album('lee', 'No.9')
# print(information)

# 8-8 用户的专辑