# 定义car的名单
cars = ['audi', 'bmw', 'subaru', 'toyota']

# 从cars名单中循环，如果car名字有符合bmw的，如果是就全大写的方式打印。如果不是，就用首字母大写的方式打印
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

