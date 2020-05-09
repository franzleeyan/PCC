# 赋值名字
# first_name = "eric"

# 用名字首字母大写的方式拼接短语
# hello_message = "Hello " + first_name.title() + ", would you like to learn some Python today?"

# 打印短语
# print(hello_message)

# 分别打印名字首字母大写，全小写，全大写
# print(first_name.title())
# print(first_name.lower())
# print(first_name.upper())

# 打印双引号的语句"A person who never made a mistake never tried anything new."
# said_message: str = 'Albert Einstein once said,"A person who never made a mistake never tried anything new."'
#
# print(said_message)

# 将名人名称赋值famous_person,并和名言拼接打印
# famous_person = "Albert Einstein"
# famous_person_said_message = '"A person who never made a mistake never tried anything new."'
#
# print(famous_person + "once said," + famous_person_said_message)

# 赋值人名，前空格或者后空格
first_name = ' \tFranz'
second_name = '\nEric '

# 打印\n \t 的人名输出模式
# print(first_name)
# print(second_name)

# 打印取消取消空格的赋值人名
print(first_name.lstrip())
print(second_name.rstrip())
print(second_name.strip())
