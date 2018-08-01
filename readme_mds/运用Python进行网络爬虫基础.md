# 运用Python进行网络爬虫基础

`网络爬虫是一个与网站进行交互的程序`。网络爬虫用于`创建搜索引擎索引`和`归档页面`。编写爬虫前，我们需要先了解网页的工作原理。特别是，需要了解一些 HTML。

## HTML 要点概述

HTML 或`超文本标记语言`是网页的源代码。HTML 文档是描述页面内容的`文本文档`。其包括`文本内容`、页面上`图像和视频的 URL `以及`关于内容排列和样式`的信息。`网页浏览器`会收到原始 HTML，并相应提供格式整齐的多媒体网页。

```html
<title>My Website</title>
<div id="introduction">
  <p>
    Welcome to my website!
  </p>
</div>    
<div id="image-gallery">
  <p>
    This is my cat!
    <img src="cat.jpg" alt="Meow!">
    <a href="https://en.wikipedia.org/wiki/Cat">Learn more about cats!</a>
  </p>
</div>
```

`HTML 源代码由嵌套标签组成`。第一个标签是标题标签，`<title>` 和结束标签 `</title>` 之间的文本用作页面标题。"

HTML 源代码中的下一个标签是 `<div id="introduction">`。`div` 是 "division" 的缩写，`id="introduction"` 表示该页面的作者将这一部分标注为引言。

我们在该标签下面的几行中可看到 `</div>`。这是 div 的结束标签，表示该段落代码嵌套在 div 中。

```html
<p>
  Welcome to my website!
</p>
```

p 是 "段落" 的缩写。`<p>` 和其结束标签 `</p>` 之间的文本是提供 HTML 时，`显示在屏幕上的内容`。可以将该段落称为 div 标签（嵌套在其中）的 "子类"。同样，div 是段落的 "父类"。总而言之，这种`父类标签和子类标签的排列创建了一个树结构`。

词汇注释：术语 "标签" 和 "元素" 密切相关，`有时可互换使用`。`标签`是一个 HTML `源码`，而`元素`是在浏览器呈现标签后用户可以看到的`可视化组件`。

HTML 文档中的第二个 div 更复杂。它还有一个作为子类的段落标签，该段落标签有自己的子类，img 和 a。这两个子类标签嵌套在 div 标签内，成为 div 的后代标签。但它们不是 div 的子类，而是 `p` 标签的子类。

在 `href` 属性中指定`链接的地址`，开始和结束标签之间的文本即`链接的文本`。

## 使用 Python 获取 HTML

### Requests-网络请求库

这里需要使用到网络请求库，我们查看 Python 文档后，发现可以使用 `request` 库，但它不是我们标准库的一部分，所以我们需要[下载](http://docs.python-requests.org/en/master/#requests-http-for-humans)该库包。

首先去终端界面通过命令行进行安装（根据 Python 安装，你可能需要使用 pip，而不是 pip3）：

```
$ pip3 install requests
```

然后打开交互式 Python 解释器测试一些请求代码：

```python
import requests

response = requests.get('https://en.wikipedia.org/wiki/Cat')
print(response.text)
print(type(response.text))
```

### Beautiful Soup-解析库

我们现在已经掌握了`如何制作网页请求和下载 html`，接下来我们了解一下`如何解析 HTML`。由于 HTML 只是文本，我们可以使用已经了解的工具对其进行解析；`循环和字符串方法`。这将极具挑战性，`HTML 是一种非常灵活的语言，这使其难以正确解析`。但好的一点是之前的程序员已经为我们解决了这个问题。

 [Beautiful Soup 库](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 
 > “`Beautiful Soup` 可解析你提供的任何内容，并为你`遍历树`材料。可以命令其'查找所有的链接'或’查找 classexternalLink 的所有链接'或'查找 url 与 "foo.com" 匹配的所有链接或'查找粗体文本的表格标题，然后将该文本发送给我。”
 
 使用 pip 安装最新版本的 Beautiful Soup：
 
 ```
$ pip3 install beautifulsoup4
```

### 指令查看安装库

`pip install xx`：如果已经安装过，再运行一次该指令，查看安装路径，会返回该库安装路径
`pip freeze`：查看 pip 安装的库

文档有一个简单方便的快速起步指导，我们可以跟着练习，熟悉使用。

## 设计程序

示例场景：查询维基百科字段内容，连续点击要查询的字段的正文的第一个链接，到最后会得到原始查询字段最直接的解释。

上面我们知道了爬虫需要的网络库，接下来我们就要考虑爬虫程序执行的步骤。我们遵循的手动过程是：

 1. 打开文章
 2. 查找当前文章中的第一个链接
 3. 单击链接
 4. 重复此过程，直到找到“哲学”文章或进入文章周期。

这个过程中的关键词是“重复”。这四个步骤过程本质上是一个循环！

### 步骤序列

在 `while` 循环中构建我们的程序：

 1. 下载当前文章的 HTML 
 2. 查找当前文章 HTNL 中的第一个链接
 3. 将当前文章中的第一个链接添加到 `article_chain` 中
 4. 暂停几秒钟，避免请求洪泛。

手动查找链接并单击时，我们的速度自然受阅读和单击速度的限制。但 Python 程序不会受到这种限制，其`循环速度将与页面下载速度一样快`。虽然这可节省时间，但是`用快速重复的请求敲击网络服务器显得无礼粗鲁`。如果`不减慢循环速度，服务器可能会认为我们是试图超载服务器的攻击者，因此会阻止我们`。服务器可能是对的！如果代码中有一个错误，我们可能会进入一个`无限循环`，并且请求将`淹没服务器`。为了避免此种情况，我们应该在主循环中暂停几秒。通过暂停几秒，`限制我们的请求速度`。

## 执行程序

### 测验 `continue_crawl` 函数

我们需要编写的第一个帮助函数是 `continue_crawl`，其将用于我们的 while 循环，`用于控制 while 循环的结束时机`。

```python
def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True
```

 - `search_history` 是维基百科文章 url 的字符串列表。
 - 如果 `target_url` 是查找到的结果，停止搜索时文章 url 的字符串。
 
 ### while 循环
 
 我们在 while 循环中执行的操作：
 
 ```python
import time

def web_crawl():
    while continue_crawl(article_chain, target_url): 
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        # TODO: YOUR CODE HERE!
        time.sleep(2)
```

第一步，`在 article_chain 中下载最后一篇文章的 html` ，我们将使用请求库 `request` 从维基百科获取 html 的命令。

第二步，`查找该 html 中的第一个链接` 将涉及使用 `BeautifulSoup` 解析该 html，以获取第一个链接的 URL。

这里将这`两个步骤合并成一个单一的函数`，其`输入将是包含维基百科文章 URL 的字符串`，`输出将是包含维基百科文章正文中第一个链接的 URL 的字符串`。我们调用此函数 `find_first_link`。

```python
while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    # delay for about two seconds
```

### `find_first_link` 查询第一个链接

`find_first_link()` 函数执行的中间步骤：

```python
def find_first_link(url):
    # get the HTML from "url", use the requests library
    response = requests.get(url)
	html = response.text
    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    # find the first link in the article
    # return the first link as a string, or return None if there is no link
```

在浏览器开发工具中找到文章文本中的第一个链接，观察标签的包含关系。

```python
url = 'https://en.wikipedia.org/wiki/Cat'
...
soup.find(id='mw-content-text').find(class_='mw-parser-output').find(class_='hatnote navigation-not-searchable').a.get('href')
# >>> '/wiki/Felidae'
```

`提取页面<a>标记中的url`

```python
for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
```

`div`元素。请注意，我们必须使用参数 `class_`，原因是 `class 是 Python 中的保留关键字`。

### 改进

我们不能仅仅寻找第一个段落中第一个出现的链接，我们真正要的是第一个段落文本中出现的第一个链接。

```python
content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.a:
        first_relative_link = element.a.get('href')
        break
```

第一行代码查找到包含文章正文的 `div`。如果该标签是 div 的子类，则下一行在 div 中循环每个 `<p>`。如果想让 Beautiful Soup 只考虑`直接子类`，可以按照 `recursive=False` 进行传递" 。

循环主体可以查看段落中是否存在 `a` 标签。如果存在，就从链接中获取 url，并将其存储在 `first_relative_link` 中，然后结束循环。

注意：我也可以使用 `children` 方法编写代码。但循环主体将有所不同。

### 再次改进

如何确保我们的代码只能查找到普通文章的链接，而不是链接到脚注、发音指南或其他奇怪的内容？

```python
content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link = element.find("a", recursive=False).get('href')
        break
```

这发挥作用的原因是 "特殊链接"（如脚注和发音键）似乎`都包含在更多 div 标签中`。由于这些`特殊链接不是段落标签的直接后代`，可以使用与之前相同的技术`跳过这些链接`。我这次使用 find 方法，而不是 find_all，原因是 `find 可返回其查找到的第一个标签`，而不是匹配标签的列表。

### 总结

`find_first_link()`完整函数内容：
```python
def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return 

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link
```
这里有一行新代码，`first_link = urllib.parse.urljoin ('https://en.wikipedia.org/', article_link)`。 我们之前获取的 `first_relative_link` 是相对 url，我们需要创建绝对 url。

## 运行完整的代码


```python
import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2) # Slow things down so as to not hammer Wikipedia's servers
```

