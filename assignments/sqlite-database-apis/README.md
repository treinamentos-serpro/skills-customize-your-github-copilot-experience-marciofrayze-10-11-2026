# 📘 Tarefa: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Na tarefa anterior, as tarefas (to-do list) ficavam guardadas em uma lista na memória, então tudo era perdido ao reiniciar o servidor. Nesta tarefa você vai usar um banco de dados SQLite para salvar as tarefas em um arquivo, de forma que os dados continuem existindo mesmo depois de desligar e ligar a API novamente.

**Pré-requisitos:** funções, dicionários, classes e a criação de APIs com FastAPI.

**Instalação:** `pip install fastapi uvicorn`

O SQLite já vem com o Python (módulo `sqlite3`), então não é preciso instalar nada extra para o banco.

**Executando a API:** `uvicorn main:app --reload` e depois acesse `http://127.0.0.1:8000/docs`.

## 📝 Tarefas

### 🛠️ Criando o Banco e a Tabela

#### Descrição
Antes de qualquer rota funcionar, o banco precisa existir e ter a tabela `tasks`. Você vai criar uma função que abre a conexão com o arquivo do banco e outra que cria a tabela, caso ela ainda não exista.

#### Requisitos
O programa completo deve:

- Criar uma função `get_connection()` que abra uma conexão com `sqlite3` usando o arquivo `tasks.db` e configure `row_factory = sqlite3.Row`, para que as linhas possam ser acessadas pelo nome das colunas
- Criar uma função `init_db()` que execute `CREATE TABLE IF NOT EXISTS tasks` com as colunas `id` (inteiro, chave primária com autoincremento), `title` (texto, obrigatório) e `done` (inteiro: `0` ou `1`, padrão `0`)
- Chamar `init_db()` assim que a aplicação iniciar
- Criar a rota `GET /` que retorne `{"message": "API de tarefas com banco de dados"}`

### 🛠️ Criação e Listagem de Tarefas

#### Descrição
Crie os modelos Pydantic e as rotas que inserem e leem tarefas no banco. Note que o `id` é gerado pelo próprio banco, então o cliente não precisa enviá-lo ao criar uma tarefa.

#### Requisitos
O programa completo deve:

- Criar um modelo `TaskCreate` com `BaseModel`, contendo `title` (texto) e `done` (booleano, padrão `False`)
- Criar um modelo `Task` com `id` (inteiro), `title` (texto) e `done` (booleano)
- Criar a rota `POST /tasks` que receba um `TaskCreate`, insira a tarefa no banco com `INSERT` e retorne a tarefa criada, incluindo o `id` gerado (use `cursor.lastrowid`)
- Criar a rota `GET /tasks` que execute `SELECT` e retorne todas as tarefas como uma lista de `Task`
- Converter `done` de inteiro para booleano na resposta (`bool(row["done"])`)
- Usar parâmetros `?` nas consultas, e não concatenar texto nas instruções SQL

### 🛠️ Consulta, Atualização e Remoção no Banco

#### Descrição
Implemente as rotas que operam sobre uma tarefa específica pelo `id`. Assim como na tarefa anterior, o caso em que a tarefa não existe precisa ser tratado com `404`.

#### Requisitos
O programa completo deve:

- Criar a rota `GET /tasks/{task_id}` que execute `SELECT ... WHERE id = ?` e retorne a tarefa
- Criar a rota `PUT /tasks/{task_id}` que execute `UPDATE` com os novos dados e retorne a tarefa atualizada
- Criar a rota `DELETE /tasks/{task_id}` que execute `DELETE` e retorne uma mensagem de confirmação
- Retornar erro `404` com `HTTPException` quando o `task_id` não existir, em todas as três rotas (use `cursor.rowcount` ou um `SELECT` antes da alteração para verificar)
- Fechar a conexão com o banco ao final de cada operação

### 🛠️ Desafio: Filtrando Tarefas e Testando a Persistência

#### Descrição
Para finalizar, você vai adicionar um filtro na listagem e comprovar que os dados sobrevivem a um reinício do servidor.

#### Requisitos
O programa completo deve:

- Alterar a rota `GET /tasks` para aceitar o parâmetro opcional `done` na URL (por exemplo, `/tasks?done=true`) e retornar apenas as tarefas que atendem ao filtro
- Quando o parâmetro não for informado, retornar todas as tarefas
- Criar algumas tarefas pelo `/docs`, desligar o servidor (`Ctrl+C`), ligá-lo novamente e verificar que as tarefas continuam lá
- Confirmar que o arquivo `tasks.db` foi criado na pasta do projeto
