# Python 控制流程

内容包括： 

* 条件语句
* 布尔表达式
* For 和 While 循环
* Break 和 Continue
* Zip 和 Enumerate
* 列表推导式

## 条件语句

### 缩进

一些其他语言使用花括号 `"{}"` 来表示代码块从哪儿开始，到哪儿结束。在 Python 中，我们`使用缩进来封装代码块`。例如，if 语句使用缩进告诉 Python 哪些代码位于不同条件语句里面，哪些代码位于外面。

在 Python 中，`缩进通常是四个空格一组`。请`严格遵守该惯例`，因为更改缩进会完全更改代码的含义。

```python
age = 35

free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

concession_ticket = 1.25
adult_ticket = 2.50

if age <= free_up_to_age:
	ticket_price = 0
elif age <= child_up_to_age:
	ticket_price = concession_ticket
elif age >= senior_from_age:
	ticket_price = concession_ticket
else:
	ticket_price = adult_ticket			

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
# 输出
Somebody who is 35 years old will pay $2.5 to ride the bus.
```

## 条件布尔表达式

### 复杂的布尔类型

If 语句有时候会使用更加复杂的条件布尔表达式。可能`包括多个比较运算符、逻辑运算符，甚至包括算式`。


```python
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
```

无论是简单还是复杂的条件，if 语句中的条件都必须是`结果为` True 或 False 的`布尔表达式	`，`该值决定了 if 语句中的缩进代码块是否执行`。

### 正反面示例

 1.请勿使用 `True` 或 `False` 作为条件
 
 ```python
# Bad example
if True:
    print("This indented code will always get run.")
```

虽然“True”是一个有效的布尔表达式，但`不是有用的条件`，因为它`始终为 True，因此缩进代码将始终运行`。同样，“if False” 也不应使用，该 if 语句之后的语句将从不运行。

```python
# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")
```

同样，使用你知道`将始终结果为 True 的条件`（例如上述示例）也是毫无用途的。布尔表达式只能为 True 或 False，因此 is_cold 或 not is_cold 将始终为 True，缩进代码将始终运行。

 2.在使用逻辑运算符编写表达式时，要谨慎
 
 ```python
# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")
```

这段代码在 Python 中是有效的，但不是布尔表达式，虽然读起来像。原因是 or` 运算符右侧的表达式 "rain" 不是布尔表达式`，它是一个字符串。稍后我们将讨论当你使用非布尔型对象替换布尔表达式时，会发生什么。

3.请勿使用 `== True` 或 `== False` 比较布尔变量

这种比较没必要，因为`布尔变量本身是布尔表达式`。

```python
# Bad example
if is_cold == True:
    print("The weather is cold!")
```

这是一个有效的条件，但是我们可以`使用变量本身作为条件`，使`代码更容易读懂`，如下所示。

```python
# Good example
if is_cold:
    print("The weather is cold!")
```

如果你想检查布尔表达式是否为 False，可以`使用 not 运算符` + 变量。

### 真假值测试

如果我们在 if 语句中使用`非布尔对象`代替布尔表达式，Python 将`检查其真假值`，`判断是否执行缩进代码块`。`默认情况下，Python 中对象的真假值被视为 True`，除非在文档中被指定为 False。

以下是在 Python 中`被视为 False` 的大多数内置对象：

* 定义为 false 的常量：`None` 和 `False`
* 任何数字类型的零：`0`、`0.0`、`Decimal(0)`、`Fraction(0, 1)`
* 空序列和空集合：`""`、`（）`、`[ ]`、`{ }`、`set()`、`range(0)`
 
```python
points = 60

prize = None

if points <= 50:
	prize = "a wooden rabbit"
elif 151 <= points <= 180:
	prize = "a water-thin mint"
elif points >= 181:
	prize = "a penguin"

if prize:
	result = "Congratulations! You have won " + prize + "!"			
else:
	result = "Oh dear, no prize this time."

print(result)		
# 输出
Oh dear, no prize this time.
```

## For 循环(Loops)
 
Python 有两种类型的循环：`for` 循环和 `while` 循环。`for 循环用来遍历可迭代对象`。

**可迭代对象**是`每次返回其中一个元素的对象`，包括字符串、列表和元组等`序列类型`，以及字典和文件等`非序列类型`。你还可以使用迭代器和生成器定义可迭代对象。

例如 `range(2, 5)` 返回一个 2 到 4 的序列。

### for 循环的组成部分

```python
# iterable of cities
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# for loop that iterates over the cities list
for city in cities:
    print(city.title())
```

1. 循环的第一行以`关键字 for` 开始，表示这是一个 for 循环。
2. 然后是 `iteration_variable in iterable`，表示正在被遍历的是`可迭代的对象`，并且用`迭代变量`表示当前正在被处理的`可迭代对象的元素`。在此示例中，迭代变量 city 在第一次迭代时将是“new york city”，在第二次迭代时将是“mountain view。

你可以随意`命名迭代变量`。常见模式是 `为迭代变量和可迭代对象指定相同的名称`，但是分别`使用单复数形式`（例如 'city' 和 'cities'）。

### 创建列表

在 for 循环的每次迭代时向新列表中添加元素，创建一个列表。

```python
# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
```

### 修改列表

修改列表需要使用新的函数 `range()`，它是一个内置函数，用于`创建不可变的数字序列`。它有三个参数，必须`都为整数`。

`range(start=0, stop, step=1)`:

`start` 是该序列的第一个数字，`stop` 是该序列的最后一个数字大1，`step` 是该序列中每个数字之间的差即 `步长`。如果未指定的话，`start` 默认为0，`step` 默认为1。

 - 如果你在 range() 的括号里`指定一个参数`，它将`用作 'stop' `的值，另外两个参数使用默认值。E.g. `list(range(4))` 返回 `[0, 1, 2, 3]`
 - 如果你在 range() 的括号里`指定两个参数`，它们将`用作 'start' 和 'stop' 的值`，'step' 将使用默认值。 E.g. `list(range(2, 6))` 返回 `[2, 3, 4, 5]`
 - 或者你可以`为三个参数 'start、stop' 和 'step' 均指定一个值`。 E.g. `list(range(1, 10, 2))` 返回 `[1, 3, 5, 7, 9]`

注意，在这些示例中，我们将 range 封装在列表中。因为 `range 本身的输出是一个 range 对象`。我们可以通过`将其转换为列表`或`在 for 循环中遍历它`，查看 range 对象中的值集合。

我们可以`使用 range 函数为 cities 列表中的每个值生成索引`。这样我们便可以使用 `cities[index]` 访问列表中的元素，以便直接修改 cities 列表中的值。

```python
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    # 使用 title 使其首字母大写
    cities[index] = cities[index].title()
```

虽然修改列表是 range 函数的一个用途，但是并非只有这一个用途。你将经常使用 range 和 for `循环重复某个操作一定的次数`。

```python
for i in range(3)
    print("Hello!")
```

```python
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += '<li>{}</li>\n'.format(item)
html_str += '</ul>\n'
print(html_str)
# 输出
<ul>
<li>first string</li>
<li>second string</li>
</ul>
```

### 循环遍历字典（Dictionaries）

`dict.items()`，返回视图对象`（key, value）`。

```python
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
# 输出
Iterating through keys:
Jason Alexander
Michael Richards
Jerry Seinfeld
Julia Louis-Dreyfus

Iterating through keys and values:
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes    
```

## While 循环

`For` 循环是一种“`有限迭代`”，意味着`循环主体将运行预定义的次数`。这与“`无限迭代`”循环不同，无限循环是指`循环重复未知次数`，并在`满足某个条件时结束`，`while` 循环正是这种情况。

```python
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  <= 17:
    hand.append(card_deck.pop())
# 输出
[10, 8]    
```

### While 循环的组成部分

1. 第一行以关键字 while 开始，表示这是一个 while 循环。
2. 然后是要`检查的条件`。在此示例中是 sum(hand) <= 17。
3. 该头部之后的缩进部分是 while `循环的主体`。如果 while 循环的条件为 true，该循环的主体将被执行。`每次运行循环主体时，条件将被重新评估`。这个检查条件然后运行循环的流程将重复，`直到该表达式变成 false`。

循环的缩进`主体应该至少修改测试表达式中的一个变量`。如果测试表达式的值始终不变，就会变成无限循环！

示例：写一个 while 循环，用于计算比整数 limit 小的最大平方数，并将其存储在变量 nearest_square 中。平方数是整数乘以自己后的积，例如 36 是一个平方数，因为它等于 6*6。

```python
limit = 40
num = 0
# write your while loop here
while (num+1)**2 < limit:
    num += 1
    nearest_square = num ** 2

print(nearest_square)
```

## Break、Continue

有时候我们需要`更精准地控制何时循环应该结束`，或者`跳过某个迭代`即某次循环。在这些情况下，我们使用关键字 break 和 continue，`这两个关键字可以用于 for 和 while 循环`。

 - break 使循环终止
 - continue 跳过循环的一次迭代

```python
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break;
print(news_ticker)
# 输出
Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
```

## Zip 和 Enumerate

zip 和 enumerate 是实用的内置函数，可以在`处理循环时用到`。

### Zip

**zip 返回一个迭代器**，zip 返回一个`将多个可迭代对象组合成一个元组序列的迭代器`。每个元组都`包含`所有`可迭代对象`中`该位置的元素`。

`list(zip(['a', 'b', 'c'], [1, 2, 3]))` 将输出 `[('a', 1), ('b', 2), ('c', 3)]`.

正如 `range()` 一样，我们需要`将其转换为列表`或使用循环进行遍历以查看其中的元素。

```python
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(*point))

for point in points:
    print(point)
# 输出
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1    
```

你可以如下所示地用` for 循环拆封`每个元组

```python
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
#输出
a: 1
b: 2
c: 3     
```

除了可以将两个列表组合到一起之外，还可以使用星号 `*` 拆封列表。

```python
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```

这样可以创建正如之前看到的相同 letters 和 nums 列表。

用 Zip 进行 `矩阵转置`，使用 zip 将 data 从 4x3 矩阵转置成 3x4 矩阵。

```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)
# 输出
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
```

### Enumerate

enumerate 是一个会返回元组迭代器的内置函数，这些元组包含`列表的索引和值`。当你`需要在循环中获取可迭代对象的每个元素及其索引时`，将经常用到该函数。

示例，使用 enumerate 修改列表 cast，使每个元素都包含姓名，然后是角色的对应身高。例如，cast 的第一个元素应该从 "Barney Stinson" 更改为 "Barney Stinson 72”。

```python
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, height in enumerate(heights):
    cast[i] += " " + str(height)

print(cast)
# 输出
['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']
```

## 列表推导式

在 Python 中，你可以使用列表推导式`快速简练地创建列表`。下面是之前的一个示例：

```python
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
```

借助列表推导式，我们使用 `for` 循环一步创建一个列表：

```python
capitalized_cities = [city.title() for city in cities]
```

我们使用方括号 `[]` 创建列表推导式，括号里包含要`对可迭代对象中的每个元素进行评估的条件`。上述列表推导式对 cities 中的每个元素 city 调用 city.title()，以为新列表 capitalized_cities 创建每个元素。

### 列表推导式中的条件语句

你还可以向列表推导式添加条件语句。`在可迭代对象之后`，你可以使用关键字 `if` 检查每次迭代中的条件。

```python
squares = [x**2 for x in range(9) if x % 2 == 0]
# 输出
[0, 4, 16, 36, 64]
```

上述代码`仅在 x 为偶数时才评估 x 的 2 次幂`。如果你想添加 else，将遇到语法错误。

```python
squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
```

如果你要添加 `else`，则`需要将条件语句移到列表推导式的开头`，`直接放在表达式后面`，如下所示:

```python
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

列表推导式并没有在其他语言中出现，但是在 python 中很常见。

例子：按得分过滤姓名，使用列表推导式创建一个 passed 的姓名列表，其中仅包含得分至少为 65 分的名字。

```python
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [key for key, value in scores.items() if value >= 65]# write your list comprehension here
print(passed)
# 输出
['Beth Smith', 'Summer Smith', 'Rick Sanchez']
```

