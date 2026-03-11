from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
#示例数据模版
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")

#示例数据的动态注入
examples_data = [
    {"word":"大", "antonym":"小"}
]

few_shot_template = FewShotPromptTemplate(
    example_prompt = example_template, # 示例数据的模版
    examples = examples_data, # 示例数据
    prefix = "告知我单词的反义词，，我提供如下的示例：", # 前缀
    suffix = "基于前缀的示例告诉我，{input_word}的反义词是？", # 后缀
    input_variables = ['input_word'], # 输入变量
)

res = few_shot_template.invoke(input={"input_word":"前"}).to_string()
print(res)

model = Tongyi(model="qwen-max")
print(model.invoke(input=res))