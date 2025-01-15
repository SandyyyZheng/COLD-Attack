import pandas as pd
from collections import Counter

# 读取CSV文件
df = pd.read_csv('suffix_0_49.csv')

# 统计prompt列中每个值的出现次数
prompt_counts = Counter(df['prompt'])

# 找出出现次数小于8的prompt
rare_prompts = {prompt: count for prompt, count in prompt_counts.items() if count < 8}

# 打印结果
print("\n出现次数小于8次的prompt及其出现次数：")
print("-" * 50)
for prompt, count in rare_prompts.items():
    print(f"出现次数: {count}")
    print(f"Prompt: {prompt}")
    print("-" * 50)

print(f"\n总计找到 {len(rare_prompts)} 个出现次数小于8次的prompt") 