#使用者訪問這個 API 時，系統會「等待 3 秒」後才回應 

from fastapi import FastAPI
import asyncio #引入async工具

app = FastAPI()

@app.get("/wait")
async def wait_3_seconds():
    await asyncio.sleep(3) #非同步等待3秒不會卡主程式
    return {"message" : "已等待3秒。 你好饅頭!"}
