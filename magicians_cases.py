# 使用循环语句时，需要注意在for……in 之后要有冒号

# 定义pizza名字
pizzas = ['bigpizza', 'dominos pizza', 'pizzahut']
# 循环打印pizza名字和总结语句
for pizzas in pizzas:
    print("I like " + pizzas.title() + ".")
    print("I really love pizza!\n")

# 定义动物名字
pets = ['dog','cat', 'tigger']
for pets in pets:
    print(pets.title())
    print("A " + pets.title() + " would make a great pet.")
    print("Any of these animals would make a great pet.\n")
