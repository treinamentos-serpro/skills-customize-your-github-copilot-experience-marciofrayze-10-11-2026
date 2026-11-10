# Código Inicial para a Tarefa de Persistência com SQLite e FastAPI
# Execute com: uvicorn main:app --reload

import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE = "tasks.db"


# Tarefa 1: Criando o Banco e a Tabela
def get_connection():
    # Abra a conexão com DATABASE, configure row_factory = sqlite3.Row e retorne-a
    pass


def init_db():
    # Crie a tabela tasks (id, title, done) com CREATE TABLE IF NOT EXISTS
    pass


app = FastAPI()
init_db()


@app.get("/")
def read_root():
    # Retorne uma mensagem de boas-vindas
    pass


# Tarefa 2: Criação e Listagem de Tarefas
class TaskCreate(BaseModel):
    # Defina os campos: title e done (padrão False)
    pass


class Task(BaseModel):
    # Defina os campos: id, title e done
    pass


@app.post("/tasks")
def create_task(task: TaskCreate):
    # Insira a tarefa com INSERT, use cursor.lastrowid e retorne a tarefa criada
    pass


@app.get("/tasks")
def list_tasks(done: bool | None = None):
    # Execute SELECT e retorne as tarefas (aplique o filtro done, se informado)
    pass


# Tarefa 3: Consulta, Atualização e Remoção no Banco
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Retorne a tarefa com o id informado ou levante HTTPException(404)
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # Execute UPDATE e retorne a tarefa atualizada ou levante HTTPException(404)
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Execute DELETE e retorne uma mensagem ou levante HTTPException(404)
    pass
