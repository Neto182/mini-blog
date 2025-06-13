# backend/models.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Modelo de Post
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    image = Column(String)

# Configuração do banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
