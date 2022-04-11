from typing import List , Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[int]
    nome: str
    sexo: str
    cor: str
    
banco: List[Animal] =[] 

@app.get('/')
def home():
    return {"Seja bem vindo(a)":"Washington"}

@app.get('/animais')
def listar_animal():
    return banco

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = uuid4()
    banco.append(animal)
    return None







