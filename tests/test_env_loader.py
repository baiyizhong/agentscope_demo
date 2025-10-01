"""
测试 env_loader 模块
"""

import os
import tempfile
from config.env_loader import load_env, get_env


def test_get_env():
    """测试获取环境变量功能"""
    # 设置测试环境变量
    os.environ["TEST_VAR"] = "test_value"
    
    # 测试获取存在的环境变量
    assert get_env("TEST_VAR") == "test_value"
    
    # 测试获取不存在的环境变量，应该返回 None
    assert get_env("NON_EXISTENT_VAR") is None
    
    # 测试获取不存在的环境变量时返回默认值
    assert get_env("NON_EXISTENT_VAR", "default") == "default"


def test_load_env(monkeypatch, sample_env_content):
    """测试加载 .env 文件功能"""
    # 创建临时目录和 .env 文件
    with tempfile.TemporaryDirectory() as temp_dir:
        env_file_path = os.path.join(temp_dir, '.env')
        with open(env_file_path, 'w') as f:
            f.write(sample_env_content)
        
        # 使用 monkeypatch 模拟 find_dotenv 返回我们的测试文件
        monkeypatch.setattr('dotenv.find_dotenv', lambda: env_file_path)
        
        # 清除可能已存在的环境变量
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("OPENAI_API_URL", raising=False)
        monkeypatch.delenv("MODEL_NAME", raising=False)
        
        # 加载环境变量
        load_env()
        
        # 验证环境变量是否正确加载
        assert get_env("OPENAI_API_KEY") == "sk-test123456789"
        assert get_env("OPENAI_API_URL") == "https://api.openai.com/v1"
        assert get_env("MODEL_NAME") == "gpt-3.5-turbo"