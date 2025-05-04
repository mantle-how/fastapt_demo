from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")

def read_root():
    return {"message" : "Hello FastAPI!"}

@app.get("/time")

def show_time():
    return {"time": f"{datetime.datetime.now()}"}

@app.get("/square/10")
def ten_square():
    return {"10的平方" : 10*10}

@app.get("/name/{name}") #檢查使用者是否輸入/hello/{name}，{name}為可以自由輸入的變數 注意：這裡不用加 f 字串，FastAPI 自己會解析 {name} 為路由參數
def say_hello(name):
    return f"Hello {name}"

@app.get("/square/{number}")
def square(number):
    number = int(number) #因為動態路由接收到的參數為型態為字串
    return {f"{number}'s square" : number*number}

@app.get("/greet")
#處理路徑: /greet?name=名字
def greet(name):
    message = f"Hello {name}"
    return {"message" : message}

@app.get("/multply")
#處理路徑:/multply?n1=數字1&n2=數字二
def multply(n1,n2):
    n1=int(n1)
    n2=int(n2)

    return {f"{n1}*{n2}" : n1*n2}