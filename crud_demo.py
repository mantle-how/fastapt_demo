from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#step1 定義資料模型
class User(BaseModel):
    name: str
    age: int
    email: str


#step2: 模擬資料庫(in memory)
fake_user_db: List[User] = []

# 解釋:
# List[User] 👉 型別註解（type hint）:
# 這裡的意思是：「我預期這個變數會是一個 User 型別的清單（list）」
# = [] 👉 初始化為空清單
# 一開始這個變數是一個空的 list（沒有任何使用者）


#step 3-1 :建立post路由 - 新增使用者
@app.post("/users")
def create_user(user: User):
    fake_user_db.append(user) #將使用者加入假的資料庫
    return {
        "message": "使用者建立成功!",
        "user" : user
    }

#step 3-2 取得所有使用者
@app.get("/users", response_model=List[User]) #response_model=模型	告訴 FastAPI「回傳要長這樣！」
def get_all_users():
    return fake_user_db


#Note
# post跟get兩個都是使用"/users" 可以這樣用是因為兩個的方法不同 get為查詢查看 post為新增

@app.get("/users/{id}", response_model=User)
def get_user(id:int):
    if id<0 or id >= len(fake_user_db):
        raise HTTPException(status_code=404 , detail = "找不到該使用者")
    
    return fake_user_db[id]

#Note:raise HTTPException(status_code=404, detail="找不到該使用者")
# 它的作用是什麼？
# 簡單講：
# # 如果某件事出錯，我們就「主動拋出錯誤」，並讓 FastAPI 自動幫你產生錯誤回應（含狀態碼與錯誤訊息）
#  意思拆解：

# 部分	                說明
# raise	                Python 用來「拋出錯誤」
# HTTPException	        FastAPI 專門設計的錯誤型別
# status_code=404	    回傳 HTTP 狀態碼 404
# detail="..."	        錯誤訊息，會出現在回應中

#PUT 更新/修改使用者資料
@app.put("/users/{id}", response_model=User)
def update_user(id:int, update_user:User):
    if id<0 or id> len(fake_user_db):
        raise HTTPException(status_code=404 , detail = "找不到該使用者")
    
    fake_user_db[id] = update_user #更換掉原本的
    return update_user 


#DELETE 刪除使用者資料
@app.delete("/users/{id}", response_model=User)
def delete_user(id:int):
    if id<0 or id> len(fake_user_db):
        raise HTTPException(status_code=404 , detail = "找不到該使用者")
    
    deleted_user = fake_user_db.pop(id) #從list中刪除該使用者的index資料
    return deleted_user