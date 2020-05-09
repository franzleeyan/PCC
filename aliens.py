# # 创建3个字典，3个不同的外星人
# alien0 = {'color': 'green', 'points': 5}
# alien1 = {'color': 'yellow', 'points': 10}
# aline2 = {'color': 'red', 'points': 15}
#
# # 把3个外星人放入到名为外星人的列表中
# aliens = [alien0, alien1, aline2]
#
# # 循环打印外星人列表
# for alien in aliens:
#     print(alien)

# 创建一个外行星人的空列表
# alines = []

# # 创建30个绿色的外星人
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     alines.append(new_alien)
#
# # 显示前5个外星人
# for alien in alines[:5]:
#     print(alien)
# print("...")
#
# # 显示创建了多少个外星人
# print("Total number of alin: " + str(len(alines)))

# 创建一个外行星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 历遍整个全部切片，将前三个属于条件的绿色外星人，更改为黄色、速度快、点数是10的
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前5个外星人
for alien in aliens[0:5]:
    print(alien)
print("...")


