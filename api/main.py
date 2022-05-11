from typing import List , Optional
from fastapi import FastApi
from pydantic import BaseModel
from uuid import uuid4

app = FastApi()

class Animal(BaseModel):
    id: Optional[str]
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

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'erro':'animal não localizado'}

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id:str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {"mensagem": "Animal removido com sucesso"}
    else:
        return {"erro": "Animal não localizado"}    






