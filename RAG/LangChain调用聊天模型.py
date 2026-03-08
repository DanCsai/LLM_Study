from os import system

from langchain_community.chat_models.tongyi import  ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
## qwen3-max 是聊天模型
model = ChatTongyi(model="qwen3-max")

# 准备消息 列表
messages = [
    SystemMessage(content="你是一个专业的唐诗作者"),  # 给定目标角色
    HumanMessage(content="写一首唐诗"), # 用户给定任务
    AIMessage(content="好的，我会写一首唐诗。锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"), # AI角色回复
    HumanMessage(content="请你按照上面的格式 再写一首诗")
]

# 调用stream流式执行
streamRes = model.stream(input = messages)

# for循环打印 通过.content来获取到返回的内容
for chunk in streamRes:
    print(chunk.content, end="", flush=True)

# 输出内容

# 《秋夜泊舟》
# 枫落寒江月似钩，孤舟系缆近沙洲。
# 渔灯数点摇星斗，雁字横天过戍楼。
# 霜气暗侵游子袂，砧声遥送故园愁。
# 何须更听清商曲，一夜乡心白尽头。
#
# 注：此诗严格遵循唐代五言律诗格律，押平水韵"十一尤"部。中二联以"渔灯摇星斗"与"雁字过戍楼"的工对勾勒秋夜江景，尾联化用庾信"枯树赋""白头吟"典故，将羁旅之思凝于霜鬓意象。全篇通过枫叶、孤舟、戍楼等典型唐诗意象，传递出深沉的时空苍茫感。


SimpleMessages = [
    ("system", "你是一个专业的唐诗作者"),  # 给定目标角色
    ("human", "写一首唐诗"), # 用户给定任务
    ("ai", "好的，我会写一首唐诗。"), # AI角色回复
    ("human", "请你按照上面的格式 再写一首诗"), # 用户给定任务
]