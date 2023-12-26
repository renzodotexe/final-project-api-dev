from sqlalchemy.orm import Session

import models
import schemas


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


def get_note_by_id(db: Session, id: int):
    return db.query(models.Note).filter(models.Note.id == id).first()


def get_existing_note(db: Session, author: str, title: str, content: str):
    return db.query(models.Note).filter(
        models.Note.author == author,
        models.Note.title == title,
        models.Note.content == content
    ).first()


def create_note(db: Session, blogpost: schemas.NoteCreate):
    db_post = models.Note(**blogpost.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_note(db: Session, id: int, blogpost: schemas.NoteUpdate):
    db_post = db.query(models.Note).filter(models.Note.id == id).first()
    if db_post:
        for field, value in blogpost.model_dump(exclude_unset=True).items():
            setattr(db_post, field, value)
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_note(db: Session, post: models.Note):
    db.delete(post)
    db.commit()
