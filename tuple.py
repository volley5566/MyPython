# Python3 元组
# Python 的元组与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号，列表使用方括号


# 1.元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# 2.创建空元组
tup1 = ()

# 3.元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup2 = (50)  # 不加逗号，类型为整型
print(type(tup2))

tup3 = (50,)  # 加上逗号，类型为元组
print(type(tup3))

# 访问元组
tup4 = ('Google', 'Runoob', 1997, 2000)
tup5 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup4[0])
print("tup2[1:5]: ", tup5[1:5])

# 修改元组 :元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup6 = (12, 34.56)
tup7 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的
# tup1[0] = 100

# 创建一个新的元组
tup8 = tup6 + tup7
print(tup8)

#  删除元组: 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup)

# 元组运算符
# 计算元素个数
len((1, 2, 3))
# 连接
(1, 2, 3) + (4, 5, 6)
# 复制
('Hi!',) * 4
# 元素是否存在
3 in (1, 2, 3)
# 迭代
for x in (1, 2, 3): print(x)

# 元组索引，截取: 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
L = ('Google', 'Taobao', 'Runoob')
# 读取第三个元素
L[2]
# 反向读取；读取倒数第二个元素
L[-2]
# 截取元素，从第二个开始后的所有元素
L[1:]

# 元组内置函数

# len(tuple)计算元组元素个数
tuple01 = ('Google', 'Runoob', 'Taobao')
len(tuple01)

# max(tuple)返回元组中元素最大值
tuple02 = ('5', '4', '8')
max(tuple02)

# min(tuple)返回元组中元素最小值
tuple03 = ('5', '4', '8')
min(tuple03)

# tuple(seq)将列表转换为元组
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple04 = tuple(list1)



