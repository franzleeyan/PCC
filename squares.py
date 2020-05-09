# # 定义个空的列表
# squares = []
# # 循环从rang函数中取1-10，1个数字
# for value in range(1, 11):
#     # 在循环过程中计算当前值的平方，并存储在square中
#     square = value ** 2
#     # 将新计算到的平方值，加入到列表squares的末尾
#     squares.append(square)
# # 打印列表squares
# print(squares)

# 定义数字列表内容0-9
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 打印数字列表中最小值
print(min(digits))
# 打印数字列表中最大值
print(max(digits))
# 打印数字列表总和
print(sum(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)