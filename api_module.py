from pydantic import BaseModel
class taskCreate(BaseModel):
    task: str
    priority: str
    category:str
    description: str
    duedate:str



