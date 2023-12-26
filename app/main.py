from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('../sqlitedb'):
    os.makedirs('../sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/notes/', response_model=list[schemas.Note])
def get_all_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes


@app.get('/notes/{note_id}', response_model=schemas.Note)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note_by_id(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="This ID does not exist.")
    return note


@app.post('/notes/', response_model=schemas.Note)
def create_new_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    existing_note = crud.get_existing_note(db, note.author, note.title, note.content)
    if existing_note:
        raise HTTPException(status_code=400, detail="A note with these values already exists. Try changing something.")
    return crud.create_note(db, note)


@app.put('/notes/{note_id}', response_model=schemas.Note)
def update_note_by_id(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    updated_note = crud.update_note(db, note_id, note)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="This ID does not exist.")
    return updated_note


@app.delete('/notes/{note_id}', response_model=None)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note_by_id(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="This ID does not exist.")
    crud.delete_note(db, note)
    return {"message": "Note permanently deleted."}
