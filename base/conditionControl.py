# Python3 条件控制
# Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

# if 语句
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else
# 注意：
# 1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。


var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键退出")


# 以下为if中常用的操作运算符:
# 操作符	描述
# <	小于
# <=	小于或等于
# >	大于
# >=	大于或等于
# ==	等于，比较对象是否相等
# !=	不等于
