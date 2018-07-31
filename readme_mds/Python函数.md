# Python 函数

学习内容：

 - 函数定义
 - 变量作用域
 - 文档字符串注释
 - Lambda 表达式
 - 迭代器和生成器


## 定义函数

 示例：

```python
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
...
cylinder_volume(10, 3)
```

### 函数头部

 1. 函数头部始终以关键字 `def` 开始，表示这是函数定义。
 2. 函数名称遵循和变量一样的命名规范。
 3. 头部始终以英文冒号 `:` 结束。
 
`函数主体`，函数完成操作的部分。

### 默认参数

我们可以向函数中添加默认参数，以便为在函数调用中未指定的参数提供默认值。

```python
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
```

在上述示例中，如果在`函数调用中`忽略了 radius，则将该参数设为 5。如果我们调用 cylinder_volume(10)，该函数将使用 10 作为高度，使用 5 作为半径。但是，如果调用 cylinder_volume(10, 7)，7 将覆盖默认的值 5。

此外注意，我们按照位置向参数传递值。可以通过`两种方式传递值`：`按照位置`和`按照名称`。下面两个函数的效果是一样的。

```python
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
```

## 变量作用域

变量作用域是指可以在程序的哪个部分 `引用或使用某个变量`。

在函数中使用变量时，务必要考虑作用域。`如果变量是在函数内创建的，则只能在该函数内使用该变量。你无法从该函数外面访问该变量`。

```python
# This will result in an error
def some_function():
    word = "hello"

print(word)
```

这意味着你可以为在`不同函数内`使用的不同变量使用`相同的名称`。

```python
# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"
```

像这样`在函数之外定义的变量依然可以在函数内访问`。

```python
# This works fine
word = "hello"

def some_function():
    print(word)

print(word)
```

注意：建议`将变量定义在所需的最小作用域内`。虽然函数可以引用在更大的作用域内定义的变量，但是通常不建议这么做，因为如果程序有很多变量，你可能不知道你定义了什么变量。

```python
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
# 输出
UnboundLocalError: local variable 'egg_count' referenced before assignment
```

上述代码导致 `UnboundLocalError`，因为 `Python 不允许函数修改不在函数作用域内的变量`。所以可更改为如下代码：

```python
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
# 输出
12
```

在函数内，我们可以成功地输出外部变量的值。因为我们只是**访问**该变量的值。当我们尝试将此变量的值**更改**或**重新赋值**为另一个值时，我们将遇到错误。`Python 不允许函数修改不在函数作用域内的变量`。

但是`上面的原则仅适用于整数和字符串`，`列表、字典、集合、类中可以在子程序中（子函数）通过修改局部变量达到修改全局变量的目的`。

## 文档字符串注释

文档使代码更容易理解和使用。函数尤其容易理解，因为它们通常使用文档字符串，简称 `docstrings`。文档字符串是一种注释，用于解释函数的作用以及使用方式。

文档字符串用`三个引号`引起来，第一行简要解释了函数的作用。如果你觉得需要更长的句子来解释函数，可以在一行摘要后面添加更多信息。在下面示例中，可以看出我们对函数的参数进行了解释，描述了每个参数的作用和类型。我们经常还会对函数输出进行说明。

```python
def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area
```

文档字符串的每个部分都是可选的。但是，提供文档字符串是一个良好的编程习惯。你可以在[此处](https://www.python.org/dev/peps/pep-0257)详细了解文档字符串惯例。

## Lambda 表达式

你可以使用 `Lambda` 表达式`创建匿名函数`，即没有名称的函数。lambda 表达式非常`适合快速创建在代码中以后不会用到的函数`。尤其对`高阶函数`或将其他函数`作为参数`的函数来说，非常实用。

```python
def multiply(x, y):
    return x * y
# 简写为
double = lambda x, y: x * y
```

### Lambda 函数组成部分

 1. `关键字 lambda` 表示这是一个 lambda 表达式。
 2. lambda 之后是该匿名函数的`一个或多个参数`（用英文逗号分隔），然后是一个英文冒号 `:`。和函数相似，lambda 表达式中的参数名称是随意的。
 3. 最后一部分是被评估并在该函数中返回的`表达式`，和你可能会在函数中看到的 return 语句很像。
 
 鉴于这种结构，`lambda 表达式不太适合复杂的函数，但是非常适合简短的函数`。
 
 ### Lambda 与 Map
 
 `map()` 是一个`高阶内置函数`，接受`函数`和`可迭代对象`作为输入，并返回一个将该函数应用到`可迭代对象的每个元素`的`迭代器`。
 
 ```python
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)
# averages = list(map(mean, numbers))
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)
# 输出
[57.0, 58.2, 50.6, 27.2]
```

### Lambda 与 Filter

`filter()` 是一个`高阶内置函数`，接受`函数`和`可迭代对象`作为输入，并返回一个由可迭代对象中的`特定元素`（该函数针对该元素会返回 True）组成的`迭代器`。

```python
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10
# short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)
# 输出
['Chicago', 'Denver', 'Boston']
```

## 迭代器与生成器

`可迭代对象`（iterables）是`每次`可以`返回一个元素`的对象，列表是最常见的可迭代对象之一。

`迭代器`（iterator）是一种`表示数据流的对象`，这与列表不同，列表是可迭代对象，但不是迭代器，因为它不是数据流。

如何使用生成器创建迭代器？

`生成器`是使用函数创建迭代器的简单方式。但是它不是创建迭代器的唯一方式。生成器通常是指`生成器函数`，但也可以指代函数生成的`迭代器对象`。

```python
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    print(x)
# 输出
0
1
2
3
4
```

上述代码是一个 `my_range` 生成器函数，它会生成一个从 0 到 x-1 的数字流。注意，该函数使用了 `yield` 而不是关键字 `return`。这样使函数能够一次返回一个值，并且每次被调用时都从停下的位置继续。`关键字 yield 是将生成器与普通函数区分开来的依据`。

示例，请自己写一个效果和内置函数 enumerate 一样的生成器函数。

```python
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for element in iterable:
        yield start, element
        start += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
# 输出
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
```

为什么使用生成器？

下面这段内容摘自[ stack overflow ](https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235)


> 生成器是构建迭代器的 “懒惰” 方式。当内存不够存储完整实现的列表时，或者计算每个列表元素的代价很高，你希望尽量推迟计算时，就可以使用生成器。但是这些元素只能遍历一次。

另一种解释如下，摘自[stack overflow](https://softwareengineering.stackexchange.com/questions/273551/should-i-prefer-python-generators-to-lists)

> 由于使用生成器是一次处理一个数据，在内存和存储的需求上会比使用list方式直接全部生成再存储节省很多资源。
> 由此区别，在处理大量数据时，经常使用生成器初步处理数据后，再进行长期存储，而不是使用 list。因为无论使用生成器还是 list，都是使用过就要丢弃的临时数据。既然功能和结果一样，那就不如用生成器。
> 但是生成器也有自己的局限，它产生的数据不能回溯，不像list可以任意选择。

如果可迭代对象太大，无法完整地存储在内存中（例如`处理大型文件`时），每次能够`使用一部分`很有用。

示例，实现一个生成器函数 chunker，接受一个可迭代对象并每次生成指定大小的部分数据。

```python
def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
# 输出
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
```


  
