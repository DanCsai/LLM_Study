from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lasname},刚生了个{gender},你帮我起个名字，简单回答"
)

# 调用fromat注入信息即可
prompt_text = prompt_template.format(lasname="王", gender="男")

## 大语言模型/聊天模型都可

model = Tongyi(model="qwen-max")
res = model.invoke(input = prompt_text)
print(res) #输出"王浩宇"

##链式调用
chain = prompt_template | model
chain_res = chain.invoke(input = {"lasname":"王", "gender":"男"})
print(chain_res) #输出"王浩宇"
