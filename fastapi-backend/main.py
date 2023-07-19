from fastapi import FastAPI, Response, status , HTTPException
from .database import conn, cursor
from .schemas import toDo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"detail" : "To-Do-List-Application"}

@app.get("/toDos")
async def toDos() -> dict:
    cursor.execute("""SELECT * FROM toDos ORDER BY id DESC LIMIT 10""")
    data = cursor.fetchall()
    json_compatible_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_data)

@app.post("/toDos", status_code=status.HTTP_201_CREATED)
async def createToDo(payload : toDo):
    cursor.execute(
        """INSERT INTO toDos (title, category, isDone) VALUES (%s,%s,%s) RETURNING * """,
        (payload.title, payload.category, payload.isDone),
    )
    todo = cursor.fetchall()
    conn.commit()
    json_compatible_item_data = jsonable_encoder(todo)
    return json_compatible_item_data

@app.delete("/toDos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteToDo(id : int):
    cursor.execute("""DELETE FROM toDos WHERE id = %s  RETURNING * """, (str(id),))
    todo = cursor.fetchone()
    if todo == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id : {id} cannot be deleted because it does not exist",
        )
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/toDos/{id}")
async def updateToDo(id: int, payload: toDo):
    cursor.execute(
        """UPDATE toDos SET title = %s, content = %s, published = %s  WHERE id = %s RETURNING *""",
        (payload.title, payload.category, payload.isDone),
    )
    todo = cursor.fetchone()
    if todo == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id : {id} cannot be delete because it does not exist",
        )
    conn.commit()
    json_compatible_item_data = jsonable_encoder(todo)
    return JSONResponse(content=json_compatible_item_data)