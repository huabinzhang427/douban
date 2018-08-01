# Python脚本编写

学习内容：

* Python 安装和环境设置
* 运行和修改 Python 脚本
* 与用户输入交互
* 处理异常
* 读写文件
* 导入本地、标准和第三方模块
* 在解释器中进行实验

## 安装 Python

检查计算机是否安装了 Python ？

在终端窗口输入指令 `python --version`，并按回车:

系统可能会显示已安装的 Python 版本是 `Python 2.7.9`。在这种情况下，表明你已经安装了 `Python 2`。如果`版本号以 3 开头`，则表明你已经安装了 `Python 3，**请勿再次安装 Python`！**

### 下载/安装 Anaconda

如果你对数据科学方面的 Python 感兴趣，强烈建议安装[Anaconda](https://www.continuum.io/downloads)，即使你已经在计算机上安装了 Python。

 [Anaconda 和 Jupyter notebook](https://classroom.udacity.com/courses/ud1111) 已经成为`数据分析的标准环境`。简单来说，Anaconda是`包管理器和环境管理器`，Jupyter notebook 可以`将数据分析的代码、图像和文档全部组合到一个web文档中`。
 
 [Anaconda 安装教程](https://www.zhihu.com/question/58033789)
 
 ### 下载/安装 Python
 
 [Python 下载](https://www.python.org/downloads/)，找到适用于你的操作系统、下载 3 开头的最新版本。
 
 如果你使用的是 Windows 设备，确保在安装过程中选中 `Add Python 3.5 to PATH` 或 `Add Python to environment variables` 选项，这样可以确保从命令行提示符窗口中访问 Python。
 
 如果你使用的是 Windows 设备，并且已经安装了 Python，但是未选中上述选项，则需要将 Python 添加到 PATH。这样的话，当你输入 python 时，可以告诉命令行运行 Python 3。如果你未选中上述选项，或者转到下一阶段时似乎不可行，请按照 Python 文档中的这些说明将 Python 添加到 PATH。
 
 ## 运行 Python 脚本
