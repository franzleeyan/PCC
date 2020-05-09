# # 定义学习的python词语和解释
# python_vocabulary = {
#     'print': '打印',
#     'for……in……': '条件判断',
#     'tittle': '首字母大写',
#     'if': '条件语句'}
#
# # 打印每个词语和解释
# for vocabulary, explanation in python_vocabulary.items():
#     print("\nVocabulary: " + vocabulary.title())
#     print("Explanation:" + explanation)

# 定义国家和河流的字典
country_river = {
    'nile': 'egypt',
    'yantze': 'china',
    'mississippi': 'america'
}

# 循环为每条河打印一条消息
for river,country in country_river.items():
    print("The " + river.title() + " runs though " + country.title() + ".")

print("\nThe country we collected is:")
for country in country_river.values():
    print(country.title())

print("\nThe river we collected is:")
for river in country_river.keys():
    print(river.title())

