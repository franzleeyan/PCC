# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# 使用字典
# print(alien_0['color'])

# 访问字典里面的值
# new_point = alien_0['points']
# print("You just earned " + str(new_point) + " points!")

# 添加键-值对
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# 创建空字典
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

# # 修改字典的值
# alien_0 = {}
# # 定义外星人的颜色并打印
# alien_0['color'] = 'green'
# print("The alien is " + alien_0['color'] + ".")
#
# # 修改外星人的颜色并打印现在外星人的颜色
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
#
# # 向右移动外星人
# # 据外星人当前速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # 这个外星人的速度一定很快
#     x_increment = 3
#
# # 新位置等于老位置加上增量
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))

# 删除键-值对
# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0)
#
# del alien_0['point']
# print(alien_0)

# 由类似对象组成的字典
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }