import pandas as pd
import sys
import os

def remove_duplicates(input_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)
    
    # 记录原始行数
    original_rows = len(df)
    
    # 去除完全重复的行
    df_unique = df.drop_duplicates()
    
    # 记录去重后的行数
    unique_rows = len(df_unique)
    
    # 构造输出文件名
    file_name, file_ext = os.path.splitext(input_file)
    output_file = f"{file_name}_no_duplicates{file_ext}"
    
    # 保存去重后的数据
    df_unique.to_csv(output_file, index=False)
    
    print(f"原始行数: {original_rows}")
    print(f"去重后行数: {unique_rows}")
    print(f"删除了 {original_rows - unique_rows} 行重复数据")
    print(f"结果已保存到: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python remove_duplicates.py <input_csv_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"错误: 文件 '{input_file}' 不存在")
        sys.exit(1)
        
    remove_duplicates(input_file) 