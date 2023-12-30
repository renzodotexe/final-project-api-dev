from sqlalchemy.orm import Session

import models
import schemas


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


def get_note_by_id(db: Session, id: int):
    return db.query(models.Note).filter(models.Note.id == id).first()


def get_note_by_author(db: Session, author: str):
    return db.query(models.Note).filter(models.Note.author == author).all()


def get_existing_note(db: Session, author: str, title: str, content: str):
    return db.query(models.Note).filter(
        models.Note.author == author,
        models.Note.title == title,
        models.Note.content == content
    ).first()


def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, id: int, note: schemas.NoteUpdate):
    db_note = db.query(models.Note).filter(models.Note.id == id).first()
    if db_note:
        for field, value in note.model_dump(exclude_unset=True).items():
            setattr(db_note, field, value)
        db.commit()
        db.refresh(db_note)
    return db_note


def delete_note(db: Session, note: models.Note):
    db.delete(note)
    db.commit()


def reset_database(db: Session):
    db.query(models.Note).delete()
    db.commit()
