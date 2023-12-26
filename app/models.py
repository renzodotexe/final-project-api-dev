from sqlalchemy import Column, Integer, String, Index
from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    content = Column(String)

    Index('unique_author_title_content', author, title, content, unique=True)

