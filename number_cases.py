# 循环从1-20并逐个打印出来
# for value in range(1, 21):
#     print(value)

# 创建一个列表，其中包含1-1000001
# number = list(range(1, 1000001))
# print(number)
# print(min(number))
# print(max(number))
# print(sum(number))

# 创建一个列表为1-10，并将各个数字立方，同时打印出来
# 第一个方法
# sp = []
# for value in range(1, 11):
#     sp1 = value ** 3
#     sp.append(sp1)
#
# print(sp)

#第二个方法
# sp = [value ** 3 for value in range(1, 11)]
# print(sp)

# 打印从1-20的奇数
# num = list(range(1, 21, 2))
# for ji in num:
#     print(ji)

# 创建一个列表，其中包含3-30可以被3整除的数字，使用for打印出来
# num_3 = []
# for value in range(3, 31 ,3):
#     num_3.append(value)
# for num in num_3:
#     print(num)