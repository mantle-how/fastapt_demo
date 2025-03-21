#main.py

from fastapi import FastAPI #引入FastApi套件
import datetime

app = FastAPI() #建立一個FastApi()應用程式物件 所有的 API 都會註冊在這個實體上

#建立首頁路由

@app.get("/") #GET方法 網址:http://localhost:8000/ NOTE:註冊一個路由，代表接收到 GET 請求時要執行這個函式

def read_root(): #自定義的處理函式，當有人訪問 / 時被呼叫
    return {"messege" : "Hello! FastApi"} #回傳json格式字典  FastAPI 會自動將字典轉成 JSON 並回傳給使用者

"""
note: app = FastAPI() : 是整個API的核心實體 
      @app.get("/") : 是註冊一個路由，只有當收到GET請求且路徑為 / 才會觸發這個函式
      回傳值會自動轉成json格式
"""
@app.get("/hello/{name}")#動態路由 使用get去檢查有沒有這串/hello/{name}，假如有就呼叫並執行下面的函數，{name}為可以自由輸入的變數 注意：這裡不用加 f 字串，FastAPI 自己會解析 {name} 為路由參數

def Say_Hello(name): #將name變數傳入這個函式中
    return {"messege" : f"Hello, {name} !"} #輸出

@app.get("/time")

def show_time():
    return{"time" : f"{datetime.datetime.now()}"}

