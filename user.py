# user_0 = {'username': 'efermi',
#           'first': 'enrico',
#           'last': 'fermi',
#           }
#
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Vlaue: " + value)

# # 创建字典
# favorite_languages = {'jen': 'python',
#                       'sarah': 'c',
#                       'edward': 'ruby',
#                       'phil': 'python',
#                       }
#
# # 用name键值打印列表中的名字
# for name in favorite_languages.keys():
#     print(name.title())

# 创建字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


# # 指定名字的人
# friends = ['phil', 'sarah']
# # 用name在字典中循环并打印
# for name in favorite_languages.keys():
#     print(name.title())
#
#     # 如果name在friends的条件中，则打印
#     if name in friends:
#         print(" Hi " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
#     # 若不在，则打印
#     else:
#         print(" Hi " + name.title() +
#               ", I am not to see your favorite language is " +
#               favorite_languages[name].title() +
#               ", please take our poll!")

# 按字母顺序历遍字典中的所有键
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# 历遍字典中的所有值
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())