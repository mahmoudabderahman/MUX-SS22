

from fastapi import Depends, FastAPI
from sqlalchemy import select
from services.backend.project.app.models import PersonCreate
from sqlmodel import Session

from app.db import get_session, init_db
from app.models import Person, PersonBase

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

    
@app.get("/persons", response_model=list[Person])
def get_persons(session: Session = Depends(get_session)):
    result = session.execute(select(Person))
    persons = result.scalars().all()
    return [Person(name=person.name, artist=person.lastname, id=person.id) for person in persons]


@app.post("/persons")
def add_song(person: PersonCreate, session: Session = Depends(get_session)):
    person = Person(name=person.name, artist=person.lastname)
    session.add(person)
    session.commit()
    session.refresh(person)
    return person