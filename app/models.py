from sqlalchemy import Column, Integer, String, Index
from database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

    Index('unique_title_content', title, content, unique=True)

