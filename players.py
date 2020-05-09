# 定义players列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # 打印列表中从第一个开始到第三个结束的名字
# print(players[0:3])
# # 打印列表中从第二个开始到第四个结束的名字
# print(players[1:4])
# # 因为没有自定开始，所以从第一个开始打印到第四个结束的名字
# print(players[:4])
# # 从指定位置，终止到列表结尾
# print(players[2:])
# # 打印列表最后三个的名字
# print(players[-3:])

# 遍历列表，用for循环使用列表中的切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())