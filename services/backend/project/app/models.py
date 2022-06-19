from email.policy import default
from sqlmodel import SQLModel, Field

class PersonBase(SQLModel):
    name: str
    lastname: str
    
class Person(PersonBase, table=True):
    id: int = Field(default=None, primary_key=True)
    

class PersonCreate(PersonBase):
    pass


