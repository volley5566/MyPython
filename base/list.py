# Python3 列表
# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员

# 创建一个列表
list01 = ['Google', 'Runoob', 1997, 2000]
list02 = [1, 2, 3, 4, 5 ]
list03 = ["a", "b", "c", "d"]

# 访问列表中的值
list04 = ['Google', 'Runoob', 1997, 2000]
list05 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list04[0])
print("list2[1:5]: ", list05[1:5])

# 更新列表： 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
list06 = ['Google', 'Runoob', 1997, 2000]
print("第三个元素为 : ", list06[2])
list06[2] = 2001
print("更新后的第三个元素为 : ", list06[2])

# 删除列表元素： 可以使用 del 语句来删除列表的的元素
list07 = ['Google', 'Runoob', 1997, 2000]
print(list07)
del list07[2]
print("删除第三个元素 : ", list07)

# Python列表脚本操作符
len([1, 2, 3]) # 长度
[1, 2, 3] + [4, 5, 6] # 组合
['Hi!'] * 4  # 重复
3 in [1, 2, 3] # 元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ") 迭代

# Python列表截取与拼接： Python的列表截取与字符串操作类型
L=['Google', 'Runoob', 'Taobao']
L[2] # 读取第三个元素
L[-2] # 从右侧开始读取倒数第二个元素: count from the right
L[1:] # 输出从第二个元素开始后的所有元素


# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x[0] # ['a', 'b', 'c']
x[0][1] # 'b'

# Python列表函数&方法
# Python包含以下函数:
# 序号	函数
# 1	len(list)
# 列表元素个数
# 2	max(list)
# 返回列表元素最大值
# 3	min(list)
# 返回列表元素最小值
# 4	list(seq)
# 将元组转换为列表

# Python包含以下方法:
# 序号	方法
# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop(obj=list[-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort([func])
# 对原列表进行排序
# 10	list.clear()
# 清空列表
# 11	list.copy()
# 复制列表








