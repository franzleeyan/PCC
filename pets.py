# 删除包含特定值的所有列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# # 定义一个函数describe_pet
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# # 调用函数多次
# describe_pet('dog', 'willie')

# 关键字实参
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(animal_type='hamster', pet_name='harry')

# 默认值
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(pet_name='willie')

# 等效的函数调用
# 一条名为willie的小狗
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('willie')

# 一只名为harry的仓鼠
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')

# 8-3T恤 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样
# def make_shirt(size, picture):
#     print("The T-shirt's size is " + size + ", and the picture is " + picture + ".")
# make_shirt('M', 'I love You')

# 8-4大号T恤 修改函数make_shirt()的函数，默认情况下，制作一件"I love Python"的大号T恤。
# 调用这个函数制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤(尺码无关紧要)
# 定义make_shirt()函数，尺码，字样(默认为"I love Python")
# def make_shirt(size, picture='I love Python'):
#     # 打印T恤尺码，和字样
#     print("The T-shirt's size is " + size + ", and the picture is " + picture + ".")
#
# # T恤为大号，默认字样
# make_shirt('L')
# # T恤为中号，默认字样
# make_shirt('M')
# # T恤为小号，字样是其他文字
# make_shirt('S', 'I love You')

# 8-5城市编写一个describe_city()的函数，它接受一座城市的名字及该城市所属国家。打印一个简单的句子
# 定义descibe_city()
def descibe_city(city_name, country_name):
    # 打印一座城市的名字及所属国家
    print(city_name.title() + " is in " + country_name.title() + ".")

descibe_city('reykjavik', 'iceland')
descibe_city('tokyo', 'japan')
descibe_city('buenos aires', 'turkey')