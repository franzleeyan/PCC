# # 创建一个用户名列表
# user_name = ['lily', 'fiona', 'angel', 'admin', 'franz']
# # 循环用户列表
# for user in user_name:
#     # 如果用户名为admin则输出
#     if user == 'admin':
#         print("Hello " + user + ", world you like to see a status report?")
#     # 如果不是则输出
#     else:
#         print("Hello " + user + ", thank you for logging in again.")

# 创建一个用户名列表，使用完整表格
user_name = ['lily', 'fiona', 'angel', 'admin', 'franz']

# if user_name:
#     for user in user_name:
#         if user == 'admin':
#             print("Hello " + user + ", world you like to see a status report?")
#         else:
#             print("Hello " + user + ", thank you for logging in again.")
# else:
#     print("We need to find some users!")


# 创建一个用户名列表，使用空表格
# user_name = []
#
# if user_name:
#     for user in user_name:
#         if user == 'admin':
#             print("Hello " + user + ", world you like to see a status report?")
#         else:
#             print("Hello " + user + ", thank you for logging in again.")
# else:
#     print("We need to find some users!")

# # 定义一组用户名
# current_users = ['lily', 'FIONA', 'angel', 'admin', 'franz']
# # 定义第二组名字包含一组里面的2个名字
# new_users = ['lILY', 'Fiona', 'florina', 'mikko', 'john']
# # 遍历列表 new_users检查是否被用了，如果是这样，就打印一条信息信息，指出需要输入别的用户名，否则打印一条消息指出这个用户名可以使用
# for new_user in new_users:
#     if new_user.lower() in [current_user.lower() for current_user in current_users]:
#         print(new_user + " This name is some one.")
#     else:
#         print(new_user + " This name is new.")

# # 建立一个空列表
# list =[]
# # 循环列表中添加1-9数字，并打印
# for number in range(1, 10):
#     list.append(number)
# print(list)
# # 循环数字在里面中，如果是1则打印并添加st，如果是2则打印并添加nd，如果是3则打印并添加rd，其他的都添加th
# for number in list:
#     if number == 1:
#         print(str(number) + 'st')
#     elif number == 2:
#         print(str(number) + 'nd')
#     elif number == 3:
#         print(str(number) + 'rd')
#     else:
#         print(str(number) + 'th')