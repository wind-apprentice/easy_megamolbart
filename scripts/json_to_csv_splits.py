import json
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# 設定檔案路徑
json_path = '/workspace/zinc_example_data/zinc_data_converted.json'  # 你的 JSON 檔案
output_dir = '/workspace/zinc_example_data'  # 輸出的資料夾
os.makedirs(output_dir, exist_ok=True)

# 設定輸出檔名
train_file = 'zinc_data_finetune_train.csv'
val_file = 'zinc_data_finetune_valid.csv'
test_file = 'zinc_data_finetune_test.csv'

# 欲保留的欄位
columns_to_keep = ['smiles']

# 讀取 JSON
with open(json_path, 'r') as f:
    data = json.load(f)

# 轉為 DataFrame，僅保留指定欄位
df = pd.DataFrame(data)
df = df[columns_to_keep].dropna()

# 切分資料（90% train，5% val，5% test）
train_df, temp_df = train_test_split(df, test_size=0.10, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# 寫入 CSV
train_df.to_csv(os.path.join(output_dir, train_file), index=False)
val_df.to_csv(os.path.join(output_dir, val_file), index=False)
test_df.to_csv(os.path.join(output_dir, test_file), index=False)

# 顯示統計
print("✅ JSON 轉換完成！")
print(f"→ 訓練集：{train_file}（{len(train_df)} 筆）")
print(f"→ 驗證集：{val_file}（{len(val_df)} 筆）")
print(f"→ 測試集：{test_file}（{len(test_df)} 筆）")
