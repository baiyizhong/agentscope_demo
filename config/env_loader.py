"""
通用的 .env 文件读取器
使用 python-dotenv 库实现
"""

from dotenv import load_dotenv, find_dotenv
import os


def load_env():
    """加载项目根目录下的 .env 文件"""
    dotenv_path = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path)


def get_env(key, default=None):
    """获取环境变量值"""
    return os.environ.get(key, default)