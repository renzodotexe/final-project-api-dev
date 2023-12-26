from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteUpdate(NoteBase):
    title: str | None = None
    content: str | None = None

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True