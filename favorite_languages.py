# # 定义被调查者名字
# favorite_languages = {'jen': 'python',
#                       'sarah': 'c',
#                       'edward': 'ruby',
#                       'phil': 'python',
#                       }
# # print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
#
# # for name, languages in favorite_languages.items():
# #     print("\nName: " + name.title())
# #     print("Langua: " + languages.title())
#
# for name, languages in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + languages.title() + ".")

# 每个名字关联的值都是一个列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# 遍历字典时，使用变量languages来依次存储字典中的每个值
for name,languages in favorite_languages.items():
    print("\n" + name.title() + " 's favorite languages are:")
    for language in languages:
        print("\t" + language.title())