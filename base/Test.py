print('hello');
print('runoob')

if True:
    print("True wo o")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")
#
# otal = item_one + \
#         item_two + \
#         item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)

########################################################
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# end 关键字 ：关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# 两个元素的总和确定了下一个数
a01, b02 = 0, 1
while b02 < 1000:
    print(b02, end=',')
    a01, b02 = b02, a01+b02