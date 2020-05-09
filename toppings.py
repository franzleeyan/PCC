# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies")

# requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")
#
# print("\nFinished making your pizza!")


# for requested_topping in requested_toppings:
#     # 确认是否点了青椒，如果有则输出为什么不能点青椒的原因
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     # 其他的食材，添加到披萨中
#     else:
#         print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# 确定列表不是空的
# requested_toppings = []
#
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# 使用多个表格
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")