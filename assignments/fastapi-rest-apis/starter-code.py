# Código Inicial para a Tarefa de APIs REST com FastAPI
# Execute com: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Tarefa 1: Primeira Rota GET
app = FastAPI()


@app.get("/")
def read_root():
    # Retorne uma mensagem de boas-vindas
    pass


# Tarefa 2: Modelos e Criação de Tarefas
class Task(BaseModel):
    # Defina os campos: id, title e done (padrão False)
    pass


tasks = []


@app.post("/tasks")
def create_task(task: Task):
    # Adicione a tarefa à lista e retorne-a
    pass


@app.get("/tasks")
def list_tasks():
    # Retorne todas as tarefas
    pass


# Tarefa 3: Consulta, Atualização e Remoção
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Retorne a tarefa com o id informado ou levante HTTPException(404)
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # Substitua a tarefa correspondente ou levante HTTPException(404)
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Remova a tarefa correspondente ou levante HTTPException(404)
    pass
