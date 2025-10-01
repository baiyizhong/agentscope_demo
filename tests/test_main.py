"""
测试 main.py 模块
"""

import sys
from io import StringIO
from main import main


def test_main_function():
    """测试 main 函数执行"""
    # 捕获标准输出
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # 执行 main 函数
    main()
    
    # 恢复标准输出
    sys.stdout = sys.__stdout__
    
    # 获取输出内容
    output = captured_output.getvalue()
    
    # 验证输出包含期望的内容
    assert "Hello from agentscope-demo!" in output
    assert "配置加载成功:" in output
    assert "API Key:" in output
    assert "API URL:" in output
    assert "Model Name:" in output