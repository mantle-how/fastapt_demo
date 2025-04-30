#這個用法的意義:第一層意義：保護資料，回傳「對外公開」的版本 :可以挑選要顯現出哪些資料
            #第二層意義：自動產生乾淨、明確的 API 文件   : 可以自訂response code 方便使用者區分各種代碼的意義
from fastapi import FastAPI
from pydantic import BaseModel , EmailStr

app = FastAPI()

#輸入用的模型 
class User(BaseModel):
    name:str
    email : EmailStr
    age : int

#回傳用的模型(對外公開的)
class PublicUser(BaseModel):
    name:str
    age : int


#建立 API 路由，並設定 response_model + status_code
@app.post("/user/public", response_model=PublicUser, status_code=201)
def create_user(user: User):
    return user

