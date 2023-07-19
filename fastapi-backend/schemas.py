from pydantic import BaseModel
from typing import Optional, Union

class toDo(BaseModel):
    title : str
    category : str
    isDone : Union[bool, None] = False

