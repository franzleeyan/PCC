# 定义一些摩托车的列表
# motorcyles = ['honda', 'yamaha','suzuki']
# print(motorcyles)

# 替换第一个摩托车名称
# motorcyles[0] = 'ducati'
# print(motorcyles)


# 定义一些摩托车的列表
# motorcyles = ['honda', 'yamaha','suzuki']
# motorcyles.append('ducati')
# print(motorcyles)

# 定义一个空的摩托车列表
# motorcyles = []

# 将摩托车名称加入到空的摩托车列表中
# motorcyles.append('honda')
# motorcyles.append('yamaha')
# motorcyles.append('suzuki')
# print(motorcyles)

# 定义一些摩托车的列表
# motorcyles = ['honda', 'yamaha','suzuki']

# 在某个位置加入一个摩托车名称
# motorcyles.insert(0, 'ducati')
# print(motorcyles)

# 定义一些摩托车的列表
motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
# 删除列表中的第一个名称
# del motorcyles[0]
# print(motorcyles)

# 删除列表中的第二个名称
# del motorcyles[1]
# print(motorcyles)

# 赋值被删除的摩托车名字，pop的作用是，删除列表中最后一个内容
# popped_motorcyles = motorcyles.pop()
# print(motorcyles)  # 打印现在的列表内容
# print(popped_motorcyles)  # 打印删除的内容

# 赋值我最后买的一台摩托车，使用pop的方式获取
# last_owned = motorcyles.pop()
# 打印我最后的一台摩托车是哪个
# print("The last motorcyle I owend was a " + last_owned.title() + ".")

# 赋值我第一个摩托车
# first_owend = motorcyles.pop(0)
# 打印我的第一台摩托车
# print('The first motorcyles I owend was a ' + first_owend.title() + '.')

# 根据值删除元素
print(motorcyles)
# motorcyles.remove('ducati')
# print(motorcyles)

# 根据赋值内容删除元素
too_expensive = 'ducati'
motorcyles.remove(too_expensive)
print(motorcyles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
