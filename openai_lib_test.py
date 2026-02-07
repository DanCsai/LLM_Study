import os

from openai import OpenAI
# 获取客户端对象

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 调用模型
resp = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "hello 你好"},
        {"role": "user", "content": "你好"},
    ]
)

# 打印响应
print(resp.choices[0].message.content)