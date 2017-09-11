# Python3 错误和异常
# 语法错误和异常

# 语法错误
# Python 的语法错误或者称之为解析错
# while True print('Hello world')
# File "<stdin>", line 1, in ?
#     while True print('Hello world')
#                    ^
# SyntaxError: invalid syntax

# 异常
# 即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常
# 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# ZeroDivisionError: division by zero

# 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined

# '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# TypeError: Can't convert 'int' object to str implicitly

# 异常处理
# 让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。
# 用户中断的信息会引发一个 KeyboardInterrupt 异常
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")

# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
# except(RuntimeError, TypeError, NameError):
#     pass

# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后
# 这个子句将在try子句没有发生任何异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# 使用 else 子句比把所有的语句都放在 try 子句里面要好，
# 这样可以避免一些意想不到的、而except又没有捕获的异常。
# 异常处理并不仅仅处理那些直接发生在try子句中的异常，
# 而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常
def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 抛出异常
# Python 使用 raise 语句抛出一个指定的异常
raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: HiThere

# raise 唯一的一个参数指定了要被抛出的异常。
# 它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
# 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# An exception flew by!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in ?
# NameError: HiThere

# 用户自定义异常
# 可以通过创建一个新的exception类来拥有自己的异常。
# 异常应该继承自 Exception 类，或者直接继承，或者间接继承
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)

raise MyError('oops!')


# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# __main__.MyError: 'oops!'

# 在这个例子中，类 Exception 默认的 __init__() 被覆盖。
# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，
# 然后基于这个基础类为不同的错误情况创建不同的子类:
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# 定义清理行为
# try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# Goodbye, world!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyboardInterrupt

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，
# 那么这个标准的清理行为就会执行。
# 这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上
for line in open("myfile.txt"):
    print(line, end="")

# 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

        # 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
