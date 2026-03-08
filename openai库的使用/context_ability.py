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
        {"role": "user", "content": "小明有两条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有三条宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物"},

    ],
    stream=True
)

# 流式输出
# print(resp.choices[0].message.content)
for chunk in resp:
    print(
          chunk.choices[0].delta.content,
          end="", #每一段中间已空格分割
          flush=True# 立刻刷新缓冲区
    )