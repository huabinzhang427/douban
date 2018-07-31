# Python数据类型和运算符

## 变量命名

在 python 中， 变量名称的命名方式是`全部使用使用小写字母`，并`用下划线区分单词`，也称为 `snack case`。

## 逻辑运算符

`and`：检查提供的所有语句是否都为 True；
`or`：检查是否至少有一个语句为 True；
`not`：翻转布尔值。

## 字符串

在 python 中，字符串的变量类型显示为 `str`。你可以使用双引号 `”` 或单引号 `’` 定义字符串。如果你要创建的字符串包含其中一种引号，你需要确保代码不会出错。

`type()`，检查变量类型非常重要，可以确保在编程时你所获得的结果是你想要的结果。不同类型，每种类型都有自己的一组不同的行为。

**我们可以用旧的对象创建新的对象，并在创建过程中更改类型。**

```python
grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))

...
# 输出为
<class 'str'>
<class 'float'>
```
python 中的方法和函数相似，但是它针对的是你**已经创建的变量**。方法特定于**存储在特定变量中的数据类型**。

### 字符串方法

![image](https://github.com/huabinzhang427/douban/blob/master/readme_imgs/20180705190244946.png)

任何专业人士都无法记住所有方法，因此知道如何通过文档查询答案非常重要。掌握扎实的编程基础使你能够利用这些基础知识查询文档，并且构建的程序比死记硬背所有 python 可用函数的人士构建的程序强大得多。

要详细了解字符串和字符串方法，请参阅[字符串方法文档](https://docs.python.org/3/library/stdtypes.html#string-methods)。

## 列表切片（Slicing）

列表中可以混合使用多种数据类型，比如

```python
lst_of_random_things = [1, 3.4, 'a string', True]
```

`slicing notation-切片记法`，我们可以使用列表切片从列表中提取多个值。记住，`前包含后不包含`。

```python
>>> lst_of_random_things = [1, 3.4, 'a string', True]
>>> lst_of_random_things[1:2]
[3.4]
```

仅返回列表中的 3.4。注意，这与单个元素索引依然不同，因为你通过这种索引`获得了一个列表`。冒号表示从冒号左侧的起始值开始，到`右侧的元素（不含）`结束。

如果你要从列表的开头开始，也可以`省略起始值`。

```python
>>> lst_of_random_things[:2]
[1, 3.4]
```

或者你要返回到列表结尾的所有值，可以`忽略最后一个元素`。

```python
>>> lst_of_random_things[1:]
[3.4, 'a string', True]
```

## 在不在列表中（in/not in）

我们还可以使用 `in` 和 `not in` 返回一个`布尔值`，表示`某个元素是否存在于列表中`，或者`某个字符串是否为另一个字符串的子字符串`。

```python
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
```

## 可变性和顺序（Mutability and Order）

**MUTABILITY**（可变性）表示`对象创建之后是否可以修改`。我们可以修改列表的值类型，因此列表是可变数据类型。我们无法修改字符串，因此字符串是不可变数据类型。

通过两个对象赋值关系，改变赋值的那个对象，观察被赋值对象是否发生变化，判断可变性。

```python
# 不可变对象
name = 'Jim'
student = name
name = 'Tim'
print(name)
print(student)
# 输出
Tim
Jim

# 列表和字符串不同，因为它们是可变的
scores = ['B', 'C', 'A', 'D', 'B', 'A']
grades = scores
print('scores: ' + str(scores))
print('grades: ' + str(grades))
scores[3] = 'B'
print('scores: ' + str(scores))
print('grades: ' + str(grades))
# 输出
scores: ['B', 'C', 'A', 'D', 'B', 'A']
grades: ['B', 'C', 'A', 'D', 'B', 'A']
scores: ['B', 'C', 'A', 'B', 'B', 'A']
grades: ['B', 'C', 'A', 'B', 'B', 'A']
```

注意，`可变对象和不可变对象变量包含的行为非常不同`。

**ORDER** 是指`对象的内容顺序是否重要`，以及是否可以利用该 ORDER 访问对象的某个部分。字符串和列表都是有序的，因此`可以使用索引`。但是它们又分别是不可变和可变。

`了解数据结构的这些信息很有用！`此外，你将发现每种数据类型有不同的方法，因此为何使用一种数据类型（而不是另一种）在很大程度上取决于这些特性，以及如何轻松地利用这些特性！

## 列表删除某些元素

删除列表中的某个元素，我们可以通过索引找到需要删除的元素，使用 `pop()` 方法即可。但是如果要删除某些元素，就需要注意了。

```python
P = [0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0,
     44, 1, 0]
for i in range(0,len(P)-1):
    if(P[i] == 0):
        P.pop(i)
print P 
```
会显示如下错误：

```
IndexError: pop index out of range
```

原因：

列表是不可随意乱删的。列表的索引在删除之前是固定的，`range()` 则按照从小到大排列。当删除一个索引所对应的值后， python 会自动把删除的位置补上来，这样就会导致从删除位置开始的索引与原索引相差1，从而出现上面的问题。

如果使用 `reversed(range())` ，这种索引是从大到小的顺序排列的。

![image](https://github.com/huabinzhang427/douban/blob/master/readme_imgs/20180716155349358.png)

## 实用列表函数

`max`，返回列表中的最大元素。最大元素的判断依据是列表中的对象类型。`数字列表`中最大的元素是最大的数字。`字符串列表`中最大的元素是按照`字母顺序排列时排在最后一位的元素`。如果列表包含不同的无法比较类型的元素，则 max() 的结果是 `undefined`。

`min()`，返回列表中的最小元素。它和 max() 函数相对立。

`sorted()`，返回一个从`最小到最大排序的列表副本`，并使`原始列表保持不变`。

```python
sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes))
# 输出
[6, 15, 34, 35, 65, 89]

我们也可以添加可选参数 `reverse = true`，按照`从大到小`的顺序排列。

```python
sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes， reverse = True))
# 输出
[89, 65, 35, 34, 15, 6]

`join()`，字符串方法，将`字符串列表作为参数`，并返回一个由 `列表元素`组成 并由`分隔符字符串` 分隔的 `字符串`。分隔符如果是逗号，应为英文逗号 `,`。忘记分隔符，不会触发错误，但会产生意外的结果。

```python
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
...
# 输出
fore
aft
starboard
port
```

在如上示例中，我们使用字符串 `"\n"` 作为分隔符，以便每个列表元素之间都有一个换行符。

`append()`，`将元素添加到列表末尾`。

```python
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
...
# 输出
['a', 'b', 'c', 'd', 'z']
```

## 元组（Tuple）

元组（`tuple`）是另一个实用`容器`。它是一种`不可变` `有序`元素数据类型。通常用来`存储相关的信息`。

```python
# 经纬度
location = {13.4125, 103.866667}
print("Latitude:", location[0])
print("Longitude:", location[1])
```

元组和列表相似。他们都存储一个`有序的对象集合`，并且可以`通过索引访问`这些对象。但是与列表不同的是，`元组不可变`，你`无法向元组中添加项目或从中删除项目，或者直接对元组排序`。

元组还可以用来`以紧凑的方式`为`多个变量赋值`。

```python
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
# 输出
The dimensions are 52 x 40 x 100
```

在定义元组时，`小括号是可选的`，如果小括号并没有对解释代码有影响，程序员经常会忽略小括号。

在第二行，我们根据元组 dimensions 的内容为三个变量赋了值，这叫做`元组解包`。你可以通过元组解包`将元组中的信息赋值给多个变量`，而不用逐个访问这些信息，并创建多个赋值语句。

如果我们不需要直接使用 dimensions 变量名，可以将这两行代码简写为一行，一次性为三个变量赋值！

```python
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
```

## 集合（Set）

集合是一个包含`唯一元素`的`可变` `无序`集合数据类型。集合的一个用途是`快速删除列表中的重复项`。

```python
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
# 输出
{1, 2, 3, 6}
```

集合和列表一样支持 `in` 运算符。和列表相似，你可以使用 `add()` 方法将元素`添加`到集合中，并使用 `pop()` 方法`删除`元素。但是，当你从集合中拿出元素时，会随机删除一个元素。注意和列表不同。集合是无序的，因此没有“最后一个元素”。

```python
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

# 输出
False
{'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
grapefruit
{'orange', 'watermelon', 'banana', 'apple'}
```

## 字典（Dictionaries）

字典（`dictionaries`）是可变数据类型，其中存储的是`唯一键到值`的映射，而不是像列表或集合一样存储的是单个对象。下面是存储元素和相应原子序数的字典。

```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
```

字典的键是`元素名称`，值是相应的`原子序数`。`键可以是任何不可变类型`，例如整数或元组，而不仅仅是字符串。`甚至每个键都不一定要是相同的类型`！`字典的键`和`列表的索引`相似，我们可以使用`方括号 [] 并在括号里放入键`，查询字典中的值或向字典中插入新值。如果方括号中键入的键不在字典中，程序会报错显示 `KeyError` ！！。

```python 
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
```

我们可以像检查某个值是否在列表中一样，使用关键字 `in` 检查键是否在字典中。我们`在查找键之前，使用 in 验证该键是否在字典中`，有可能该键不在字典中。

字典有一个也很有用的相关方法，叫做 `get(键)`。get 会在字典中查询值，但是和方括号不同，如果没有找到键，get 会返回 `None`（或者你所选的默认值）。

```python
print("carbon" in elements)
print(elements.get("dilithium"))
# 输出
True
None
```

我们也可以指定一个默认值，当键没找到时，`get(键， 默认值)` 返回该值。

```python
population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
m = population.get("Nanjing")
n = population.get("Nanjing", "There's no such element!");
print(m)
print(n)
# 输出
None
There's no such element!
```

carbon 位于该字典中，因此输出 True。dilithium 不在字典中，因此 get 返回 `None`，然后系统输出 None。`如果你预计查询有时候会失败，get 可能比普通的方括号查询更合适，因为错误可能会使程序崩溃`。

## 恒等运算符（is/is not）

|关键字|运算符|
|---|---|
|`is`|检查两边是否恒等|
|`is not`|检查两边是否不恒等|

我们可以用 `is` 运算符检查键是否返回了 None ，或者使用 `is not` 检查相反的情况。

```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 3}
print(elements["hydrogen"])
print(elements.get("a"))
n = elements.get("a")
print(n is None);
print(n is not None)
# 输出
1
None
True
False
```

`==（相等）` 与 `is（恒等）` 的关系？

`==` 相等只要求内容等式两边`内容`（格式，类型等）相同。而 `is` 全等则更为严格，不光要求内容，还要求`对象`相同。

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
# 输出
True
True
True
False
```

## 复合数据结构

`容器中包含容器`，以创建复合数据结构。

字典中嵌套字典：
```python
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
# 输出
{'number': 2, 'weight': 4.002602, 'symbol': 'He'}
```

## 总结

|Data Structure|	Ordered	|Mutable|	Constructor|	Example|
|---|---|---|---|---|
|int|	NA	|NA|	int()|	5
|float|	NA	|NA	|float()	|6.5
|string|	Yes|	No|	' ' or " " or str()|	"this is a string"
|bool	|NA	|NA	|NA|	True or False
|list	|Yes|	Yes	|[ ] or list()	|[5, 'yes', 5.7]
|tuple	|Yes|	No|	( ) or tuple()	|(5, 'yes', 5.7)
|set	|No|	Yes|	{ } or set()|	{5, 'yes', 5.7}
|dictionary|	No|	Keys: No|	{ } or dict()|	{'Jun':75, 'Jul':89}
