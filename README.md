# My First Spider Program

## 目的
* 練習寫 Python 程式
* 練習使用 AWS RDS

## 開發環境與工具
* windows10 & OSX
* sublime text3
* AWS RDS

## 爬蟲程式說明
```
  因為平常就有在關注台股, 所以這次就選擇來爬台股的每日交易訊息

  使用的是 臺灣證券交易所(http://www.twse.com.tw) 的 API

  說是爬蟲其實覺得也不算, 因為存粹只是去 Get 某一個頁面, 在Url上帶參數而已
  
  原理很簡單
      1. 打 api 參數 [股票代號][查詢日期]
      2. 取得資料 JSON 字串
      3. 將 JSON 字串轉換成自訂物件
      4. 使用 PyMySQL 模組 將資料存到 DB裡

  使用方法
      1. 執行 get_stock_daily_info.py
      2. 輸入 股票代碼
      3. 輸入 起始日月 (西元年+月 六碼)
      4. 開始抓取
      
  備註
      寫得很陽春並沒有加入甚麼防呆機制, 因為是想抓歷史以來的數據, 
      所以在使用上只要輸入起始日期就會把起始日期到昨天的該股票每日交易資訊抓下來
```

## 難處與學習之處

* 程式架構
```
  因為程式範圍不大, 但又不想要所有的檔案都在同一個資料夾下面,
  所以這是我面臨的第一個問題, 在多次調整後大致就分為
    主資料夾 - 主程式
    Module - 與資料庫相關
    Function - 運算邏輯相關
  
  自己看下來其實還是有點隨便, 之後會再找找一些案例來看看別人的架構是怎麼規劃的
```

* DB 連線
```
  這次選用 MySQL 來當資料庫, 就順便練習使用 AWS RDS
  其實架設起來沒甚麼困難, 因為 AWS 的教學文件寫得夠清楚了
  在使用 PyMySQL 連線也很簡單
  唯一遇到的是我在 Insert Data 的效能問題
  因為我的寫法是一天一天的資料去 Insert 這樣一個月就有 20次的連線次數
  這樣的方法我覺得應該不是標準作法, 也還在嘗試要換個怎麼樣的方式可以一次 Insert 一個月的資料
```
