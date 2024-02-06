from fastapi import FastAPI,UploadFile,Form,Response,Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from typing import Annotated
import sqlite3

# client = MongoClient()
# db = client.dest_database
# collection = db.test_collection


con = sqlite3.connect('db.db',check_same_thread=False)
cur = con.cursor() #디비에서 커서라는 개념이 있는데 인서트 셀렉트 할 때 사용

cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                image BLOB,
                price INTEGER NOT NULL,
                description TEXT,
                place TEXT NOT NULL,
                insertAt INTEGER NOT NULL
            );
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            );
            """)

app = FastAPI()

#엑세스코드를 어떻게 인코딩할지 정한다. 이게 노출되면 디코딩이 될 수 있다. 노출시키면 JWT 해석이 가능하다.
SERCRET = 'super-coding'
manager = LoginManager(SERCRET,'/login')

@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENTS = f'''id="{data}"'''
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute(f"""
                       SELECT * from users WHERE {WHERE_STATEMENTS}
                       """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()], 
           password:Annotated[str,Form()]):
    user = query_user(id)
    if not user:
        # 에러메시지 던진다. 401을 자동으로 내려준다.
        raise InvalidCredentialsException 
    elif password != user['password']:
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(data={
       'sub': {
            'id':user['id'],
            'name':user['name'],
            'email':user['email']
        }
    })
    # 자동으로 200상태코드를 내려줌
    return {'access_token':access_token}

@app.post('/signup')
def signup(id:Annotated[str,Form()], 
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    cur.execute(f"""
                INSERT INTO users(id,name,email,password)
                VALUES('{id}','{name}','{email}','{password}')
                """)
    con.commit()
    return '200'

@app.post('/items')
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()],
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]
                ):
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO 
                items (title,image,price,description,place,insertAt)
                VALUES
                ('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
                """) #자바스크립트의 `` 같은 역할
    con.commit()
    return '200'
    
@app.get('/items')
async def get_items(user=Depends(manager)):
    # 컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute("""
                       SELECT * FROM items;
                       """).fetchall()
    
    return JSONResponse(jsonable_encoder(dict(row) for row in rows))

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    #16진법을 변화해서 가져온다.
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

