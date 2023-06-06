# 111-2_ML_teamC_Baseball_Stats 一些說明

-----
## 資料夾：
### Stats: 存放 csv 檔，包含球員數據、薪資資料等相關數據
### Web Crawl: 爬蟲程式碼
### SQL & DB: SQL指令、資料庫建檔程式碼
### ML: Machine Learing 程式碼
### final: 期末報告的程式碼與資料
-----
0519 更（黃）
### 合併 standard & salary，取用 standard_salary.scv
### 合併 statcast & standard & salary，取用 new_statcast_standard_salary.scv
ps. 1. 變數表我之後會補充 2. 如果需要看處理過程，我放在 stats / data_clean_merge_0514_HPJ.ipynb /
<br>

0503 更（黃）
### 需要球員季賽表現，取用 player_performance_standard.scv
(player_performance_standard.scv 須留意有些球員在特定年度轉隊資料上會出現斷層，尚待更正)<br>
### 需要球員 statcast 數據，取用 player_performance_statcast.scv
(player_performance_statcast.scv 須留意有些球員沒有數據)<br>

需要資料處理原始檔請至 Stats 資料夾找 getGitFile.ipynb
