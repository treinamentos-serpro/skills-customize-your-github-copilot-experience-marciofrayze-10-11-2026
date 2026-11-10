# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST em Python com o framework FastAPI. Você vai implementar rotas para criar, listar, atualizar e remover tarefas (to-do list), validar dados com Pydantic e consultar a documentação gerada automaticamente.

**Pré-requisitos:** funções, dicionários e classes em Python.

**Instalação:** `pip install fastapi uvicorn`

**Executando a API:** `uvicorn main:app --reload` e depois acesse `http://127.0.0.1:8000/docs`.

## 📝 Tarefas

### 🛠️ Primeira Rota GET

#### Descrição
Crie a aplicação FastAPI e uma rota que retorne uma mensagem de boas-vindas. Em seguida, use a documentação interativa (`/docs`) para testar a rota.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI` chamada `app`
- Definir a rota `GET /` que retorne um dicionário, por exemplo `{"message": "Bem-vindo à API de tarefas!"}`
- Testar a rota pelo navegador ou pela página `/docs`

### 🛠️ Modelos e Criação de Tarefas

#### Descrição
Defina um modelo de dados com Pydantic para uma tarefa e crie a rota que adiciona novas tarefas à lista.

#### Requisitos
O programa completo deve:

- Criar um modelo `Task` com `BaseModel`, contendo `id` (inteiro), `title` (texto) e `done` (booleano, padrão `False`)
- Manter as tarefas em uma lista em memória
- Criar a rota `POST /tasks` que receba uma tarefa no corpo da requisição, adicione-a à lista e a retorne
- Criar a rota `GET /tasks` que retorne todas as tarefas

### 🛠️ Consulta, Atualização e Remoção

#### Descrição
Implemente as rotas que operam sobre uma tarefa específica identificada pelo `id` na URL e trate os casos em que a tarefa não existe.

#### Requisitos
O programa completo deve:

- Criar a rota `GET /tasks/{task_id}` que retorne a tarefa correspondente
- Criar a rota `PUT /tasks/{task_id}` que substitua os dados da tarefa
- Criar a rota `DELETE /tasks/{task_id}` que remova a tarefa da lista
- Retornar erro `404` com `HTTPException` quando o `task_id` não existir
- Verificar no `/docs` que todas as rotas aparecem documentadas com seus modelos de entrada e saída
