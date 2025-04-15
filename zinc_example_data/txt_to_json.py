import pandas as pd
import json

# 輸入與輸出檔案路徑
input_path = "zinc_data_example.txt"
output_path = "zinc_data_converted.json"

# 使用 pandas 讀取，會自動處理 tab 分隔與缺失欄位
df = pd.read_csv(input_path, sep="\t")

# 轉成 JSON 格式：每列是一個 dict，欄位名稱為 key
json_data = df.to_dict(orient="records")

# 儲存成漂亮的 JSON 檔案
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print(f"✅ 完成轉換，共 {len(json_data)} 筆資料，儲存在 {output_path}")
