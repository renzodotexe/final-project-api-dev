from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
import crud
import models
import schemas
import os

if not os.path.exists('../sqlitedb'):
    os.makedirs('../sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/notes/author/{author}", response_model=List[schemas.Note])
def get_note_by_author(author: str, db: Session = Depends(get_db)):
    note = crud.get_note_by_author(db, author=author)
    if not note:
        raise HTTPException(status_code=404, detail=f"No notes found by author: {author}")
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
def delete_note(note_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    note = crud.get_note_by_id(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="This ID does not exist.")
    crud.delete_note(db, note)
    return {"message": "Note permanently deleted."}


@app.delete("/reset-database")  # SECURED
def reset_database(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    crud.reset_database(db)
    return {"message": "Database reset successfully."}


# ---- USERS


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )

    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}
