# 创建一个我的食物列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# 创建一个我的朋友食物列表
# friend_foods = my_foods[:]
# # 不指定索引的情况下从列表my_foods中提取一个切片复制到my_foods中
# print("My favorite foods are:")
# print(my_foods)
#
# # 因此两个打印出来的食物列表是相同的
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 重复上述操作，并分别向两者列表中注入不同的食物
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')


print("My favorite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())
