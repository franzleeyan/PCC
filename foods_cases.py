# my_foods = ['pizza', 'falafel', 'carrot cake']
#
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# for my_food in my_foods:
#     print(my_food.title())
#
# print("\nMy friend's favorite foods are:")
# for friend_food in friend_foods:
#     print(friend_food.title())


squares = [value ** 2 for value in range(1, 11)]
print(squares)
print("The first three items in the list are:")
print(squares[0:3])
print("Three item from the middle of the list are:")
print(squares[5:8])
print("The last three items in the list are:")
print(squares[-3:])

