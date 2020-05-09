# 在字典中存储字典
# 创建users字典，并存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

# 遍历字典中的user，并以此存储在变量username中，并依次将当前键相关联的字典存储在变量user_info中
for username, user_info in users.items():
    # 将用户名打印出来
    print("\nUsername: " + username)
    #
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())