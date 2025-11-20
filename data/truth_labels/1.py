import pandas as pd

# 读取你的文件
df = pd.read_csv("truth_labels.csv")

# 修正 sample_id：转为字符串并补零到 3 位 (例如 3 -> "003")
df['sample_id'] = df['sample_id'].apply(lambda x: f"{int(x):03d}")

# 保存回去 (覆盖原文件)
df.to_csv("truth_labels_fixed.csv", index=False)
print("修复完成！生成了 truth_labels_fixed.csv")