# 8.3 返回值
# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回简洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 8.3.2 让实参变成可选的
# def get_formatted_name(first_name, middle_name, last_name):
#     """返回简洁的姓名"""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('jimi', 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_name, middle_name, last_name=''):
#     """返回简洁的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' +last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     # full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('jimi', 'lee', 'hooker')
# print(musician)

