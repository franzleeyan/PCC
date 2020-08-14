# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
#
# greet_user()

# def greet_user(username):
#     """显示简单的问候语"""
#     print("Hello, " + username.title() + "!")
#
# greet_user('jesse')

# 8.1case
# 编写一个名为display_message()的函数
# 打印一个句子，指出你在本章学的是什么
# def display_message():
#     """显示本章学的内容"""
#     print("本章学习了函数的设置")
# display_message()

# 8.2case
# 编写一个名为favorite_book的函数，其中包含一个名为title的形参
# 这个函数打印一条消息
def favorite_book(title):
    """显示书籍的名字"""
    print("One of my favorite books is " + title.title() + ".")
favorite_book('alice in wonderland')
