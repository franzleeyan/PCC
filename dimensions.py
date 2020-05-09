# 定义元组
dimensions = (200, 50)
# 分别打印元组
# print(dimensions[0])
# print(dimensions[1])

# 循环打印元组
# for dimensions in dimensions:
#     print(dimensions)

# 修改元组并打印
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)