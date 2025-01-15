import pandas as pd
import glob
import os
import re

# 获取当前目录下所有的csv文件
csv_files = glob.glob('suffix_*.csv')

# 定义一个函数来提取文件名中的第一个数字
def get_first_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

# 按照文件名中的第一个数字排序
csv_files.sort(key=get_first_number)

# 用于存储所有数据框的列表
dfs = []

# 读取每个CSV文件
for file in csv_files:
    print(f"正在处理文件: {file}")
    df = pd.read_csv(file)
    dfs.append(df)

# 合并所有数据框
merged_df = pd.concat(dfs, ignore_index=True)

# 删除重复行（如果有的话）
merged_df = merged_df.drop_duplicates()

# 保存合并后的文件
merged_df.to_csv('suffix_0_50.csv', index=False)

print(f"\n合并完成！共处理了 {len(csv_files)} 个文件")
print(f"合并后的文件行数: {len(merged_df)}")
print("\n处理的文件顺序：")
for file in csv_files:
    print(file) 