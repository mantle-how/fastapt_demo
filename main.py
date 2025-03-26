#main.py

from fastapi import FastAPI #引入FastApi套件
import datetime
from pydantic import BaseModel, EmailStr ,Field #匯入Pydantic import BaseModel(建立資料模型)和EmailStr(自動驗證email格式) Field(能輸入驗證條件)

app = FastAPI() #建立一個FastApi()應用程式物件 所有的 API 都會註冊在這個實體上

#day2 Step 1：定義 Pydantic 資料模型並加入驗證條件
class User(BaseModel): #定義一個python 類別 他是繼承BaseModel這個類別
    name : str = Field(...,min_length=2,max_length = 50, description = "使用者名稱: 2~50個字")#至少兩字，最多五十字
    email:EmailStr = Field(...,description="有效的email格式")# 自動驗證格式，例如 mantou@gmail.com
    age:int = Field(..., gt = 0, le=120 , description = "年齡必須為1~120歲之間") #	年齡 > 0 且 ≦ 120

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


#day2 step2 建立post路由 接收並驗證json資料
@app.post("/user")
def create_user(user:User):
    return {
        "messege":"使用者建立成功",
        "User" : user 
    }