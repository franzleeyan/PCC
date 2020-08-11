# 询问用户租赁什么牌子的汽车
# message = input('Please enter the car brand you want to rent: ')
# print('\nLet me see if I can find you a ' + message + '.')

# 询问用户多少人用餐，如果超过8人，指出没有空桌，否则有空桌
# number = input('How many people dine: ')
# number = int(number)
#
# if number <= 8:
#     print('Now free table.')
# else:
#     print('Sorry, there is no empty table.')

# 输入一个数字，并指出这个数字是否是10的整数倍
number = input('Please enter the number you need to judge whether it is an integer multiple of 10: ')
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is even. ")
else:
    print("\nThe number " + str(number) + " is odd.")
