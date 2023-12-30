from pydantic import BaseModel


class NoteBase(BaseModel):
    author: str | None = None
    title: str
    content: str


class NoteUpdate(NoteBase):
    title: str | None = None
    content: str | None = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    class ConfigDict:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class ConfigDict:
        from_attributes = True
