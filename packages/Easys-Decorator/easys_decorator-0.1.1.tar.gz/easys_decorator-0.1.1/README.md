好的,这里是一个基于你的建议修改为中文的README.md文件模板:

# Easy-Decorator

Easy-Decorator (EasyD) 是一个旨在简化装饰器创建和使用的Python库。它提供了一系列有用的装饰器和工具,帮助您轻松地创建自定义装饰器。

## 功能特性

- 使用 `decorator_factory` 简化装饰器的创建
- 常见函数装饰器: `timer`, `retry`
- 类装饰器: `singleton` 
- 异步装饰器: `async_retry`
- 可扩展的架构,支持添加自定义装饰器

## 安装

您可以使用 pip 安装 Easy-Decorator:

```bash
pip install Easys-Decorator
```

## 快速入门

以下是一个使用 Easy-Decorator 的快速示例:

```python
from EasyD import timer

@timer
def my_function():
    # 您的代码在此
    for i in range(1000000):
        pass

my_function()
# 输出: my_function 用时 0.05 秒
```

## 使用方法

### 装饰器工厂

轻松创建自定义装饰器:

```python
from EasyD import decorator_factory

def before_func():
    print("在函数执行之前")

def after_func(result):
    print(f"在函数执行之后,结果为: {result}")

@decorator_factory(before=before_func, after=after_func)
def my_function():
    return "Hello, World!"

my_function()
# 输出:
# 在函数执行之前
# 在函数执行之后,结果为: Hello, World!
```

### 重试装饰器

自动重试失败的函数:

```python
from EasyD import retry
import random

@retry(max_attempts=3, delay=1)
def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("随机错误")
    return "成功!"

result = unreliable_function()
print(result)
```

### 单例装饰器

确保一个类只有一个实例:

```python
from EasyD import singleton

@singleton
class DatabaseConnection:
    def __init__(self):
        print("初始化数据库连接")

# 这将只打印一次"初始化数据库连接"
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

## 贡献

欢迎贡献! 请随时提交 Pull Request。

## 许可证

本项目采用 MIT 许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

## 联系方式

如果您有任何问题或反馈,请在 GitHub 上提交 Issue,或联系 [SoulCodingYanhun](mailto:zhuzhishengzhu6@outlook.com)。