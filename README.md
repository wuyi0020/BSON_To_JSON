# BSON_To_JSON UGUI版本
BSON_To_JSON
# 作用
遍歷檔案夾下所有txt檔案 把檔案夾內副檔名為txt的BSON檔案轉換成JSON檔案
注意 BSON檔案副檔名需更改名為 .txt
# 使用方式
## 安裝套件
pip bson
諾有缺失套件自行補漏
---
## 開啟
右鍵bson2json.py > 開啟檔案... > Python
或 python bson2json.py
選擇要開啟的檔案夾 程式會尋找檔案夾內的"所有txt檔" 包括子檔案夾
## 完成
轉換完成後 畫面會顯示 OK
此時檔案夾內會多出一個.json檔案
諾發現檔案無法轉換 有可能原檔案並不是BSON檔案 或副檔名未更改
