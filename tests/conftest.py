"""
pytest 配置文件
"""

import sys
from pathlib import Path

# 将项目根目录添加到 Python 路径中
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


import pytest


@pytest.fixture
def sample_env_content():
    """提供示例环境变量内容用于测试"""
    return """
OPENAI_API_KEY=sk-test123456789
OPENAI_API_URL=https://api.openai.com/v1
MODEL_NAME=gpt-3.5-turbo
"""