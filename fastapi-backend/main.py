from fastapi import FastAPI, Response, status , HTTPException
# from .database import conn, cursor
from schemas import toDo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse 
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


dummyData = [{"id":"1","title":"Dishes", "category": "Housework","isDone" : False, "dateCreated" : "Today"},{"id":"2","title":"Homework", "category": "Schoolwork","isDone" : True, "dateCreated" : "Today"},
{"id":"3","title":"Meet friends", "category": "Leisure","isDone" : False, "dateCreated" : "Today"}]

@app.get("/")
def root():
    return {"detail" : "To-Do-List-Application"}

@app.get("/toDos")
async def toDos() -> dict:
    # cursor.execute("""SELECT * FROM toDos ORDER BY id DESC LIMIT 10""")
    # data = cursor.fetchall()
    json_compatible_data = jsonable_encoder(dummyData)
    return JSONResponse(content=json_compatible_data)

@app.post("/toDos", status_code=status.HTTP_201_CREATED)
async def createToDo(payload : toDo):
    # cursor.execute(
    #     """INSERT INTO toDos (title, category, isDone) VALUES (%s,%s,%s) RETURNING * """,
    #     (payload.title, payload.category, payload.isDone),
    # )
    # todo = cursor.fetchall()
    # conn.commit()
    payload["id"] = random.randint(1000000,9999999)
    payload["datecreated"] = "today"
    dummyData.append(payload)
    json_compatible_item_data = jsonable_encoder(payload)
    return json_compatible_item_data

@app.delete("/toDos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteToDo(id : int):
    # cursor.execute("""DELETE FROM toDos WHERE id = %s  RETURNING * """, (str(id),))
    # todo = cursor.fetchone()
    # if todo == None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"todo with id : {id} cannot be deleted because it does not exist",
    #     )
    # conn.commit()
    for dictionary in dummyData:
        if dictionary.get("id") == id:
            # Remove the dictionary from the array
            dummyData.remove(dictionary)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/toDos/{id}")
async def updateToDo(id: int, payload: toDo):
    # cursor.execute(
    #     """UPDATE toDos SET title = %s, content = %s, published = %s  WHERE id = %s RETURNING *""",
    #     (payload.title, payload.category, payload.isDone),
    # )
    # todo = cursor.fetchone()
    # if todo == None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"todo with id : {id} cannot be delete because it does not exist",
    #     )
    # conn.commit()

    for dictionary in dummyData:
        if dictionary.get("id") == id:
            print("matching dict")
            for key, value in payload.items():
                if key in dictionary:
                    dictionary[key] = value
                    a = dictionary
    json_compatible_item_data = jsonable_encoder(a)
    return JSONResponse(content=json_compatible_item_data)