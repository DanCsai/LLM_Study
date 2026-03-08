# 大语言模型
from langchain_community.llms.tongyi import Tongyi
from langchain_community.llms.ollama import Ollama

## 通义模型
model =Tongyi(model="qwen-max")

#调用invoke向模型提问
res = model.invoke(input = "你是谁？能做什么？")
print(res)


## ollama本地模型
ollamaModel =Ollama(model="qwen3-vl:4b")
ollamaRes = ollamaModel.invoke(input = "你是谁？能做什么？")
print(ollamaRes)


## 流式输出
streamRes = model.stream(input = "你是谁？能做什么？")
for chunk in streamRes:
    print(chunk, end="", flush=True)
