# # 创建一个名为 sandwich_orders 的列表
# sandwich_orders = ['toasted sandwich', 'pastrami', 'tuna sandwich', 'pastrami', 'club sandwich', 'pastrami']
#
# # 创建一个名为 finished_sandwich 的列表
# finished_sandwichs = []
#
# print("The five cigarette pastrami at the deli is sold out.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
#
# # 遍历 sandwich_orders 对于每种三明治，都打印一条消息，并将其移动到 finished_sandwich
# while sandwich_orders:
#     finished_sandwich = sandwich_orders.pop()
#     print("I made your " + finished_sandwich.title() + ".")
#     finished_sandwichs.append(finished_sandwich)
#
# # 所有三明治都做好后，打印一条信息，将这些三明治列出来
# # print("\nThe finishedwich is:")
# # for finished_sandwichs in finished_sandwichs:
# #     print(finished_sandwichs.title())
#
# print(finished_sandwichs)
# print(sandwich_orders)

# 使用 sandwich_orders 的内容
# 打印一条信息，指出熟食店的五香烟熏牛肉卖完了
# 在用一个while循环将列表 sandwich_orders 中的 'pastrami' 删除
# 确认最终的列表 finished_sandwiches 中不包含pastrami

# 设置一个标志，指出调查是否继续
responses = {}

polling_active = True

while polling_active:
    # 提示用户输入梦想的度假胜地
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, where would you go?")

    # 将答案存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let anther person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would visit go to " + response + ".")