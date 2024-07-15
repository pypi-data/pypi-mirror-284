from .core.base import decorator_factory
from .function.basic import timer, retry
from .class_decorators.basic import singleton
from .async_decorators.basic import async_retry

__all__ = ['decorator_factory', 'timer', 'retry', 'singleton', 'async_retry']

# 为简化导入,添加一个简短的别名
import sys
sys.modules['EasyD'] = sys.modules[__name__]