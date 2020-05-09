# 用一个自助餐馆的菜单定义元组
dimensions_menu = ('fries', 'hamburg', 'bacaon', 'sandwich', 'steak')
print("This is our menu:")
# 添加一个元组内容，并打印
# dimensions_menu[0] = ('pasta')
# 循环打印菜单中的元组
# for menu in dimensions_menu:
#     print(menu.title())
for menu in dimensions_menu:
    print(menu.title())

dimensions_menu = ('fries', 'hamburg', 'bacaon', 'sandwich', 'steak', 'pasta', 'salad')
print("\nThis is our new menu:")

for menu in dimensions_menu:
    print(menu.title())