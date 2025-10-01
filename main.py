from config.env_loader import load_env, get_env

def main():
    # 加载 .env 文件中的环境变量
    load_env()
    
    # 获取配置信息
    api_key = get_env("OPENAI_API_KEY","SK")
    api_url = get_env("OPENAI_API_URL","")
    model_name = get_env("MODEL_NAME","")
    
    print("Hello from agentscope-demo!")
    print(f"配置加载成功:")
    print(f"  API Key: {api_key[:10]}...")  # 只显示前10位以保护隐私
    print(f"  API URL: {api_url}")
    print(f"  Model Name: {model_name}")


if __name__ == "__main__":
    main()