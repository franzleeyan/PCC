# 赋值年龄
age = 12
#
# # 如果年龄小于4则打印if下的语句，要是大于4小于18岁，则打印elif下的语句，如果都不符合，则打印else下的语句
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")


# 简单的if-elif-else用法
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
#
# print("Your admission cost is $" + str(price) + ".")

# 简单的if-elif-else用法，使用多个elif代码段
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")





