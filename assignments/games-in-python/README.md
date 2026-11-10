
# 📘 Tarefa: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras usando strings, loops, condicionais, seleção aleatória e entrada de dados do usuário em Python.

## 📝 Tarefas

### 🛠️ Seleção de Palavra e Progresso

#### Descrição
Crie o início do jogo da Forca: escolha uma palavra aleatoriamente de uma lista predefinida e mostre ao jogador o progresso atual, com cada letra ainda não descoberta representada por `_`.

#### Requisitos
O programa completo deve:

- Selecionar palavras aleatoriamente de uma lista predefinida
- Exibir o progresso atual no formato `_ _ _`, revelando as letras já adivinhadas

### 🛠️ Palpites e Tentativas

#### Descrição
Implemente o laço principal do jogo, em que o jogador informa letras e o programa atualiza o progresso e controla as tentativas restantes.

#### Requisitos
O programa completo deve:

- Aceitar palpites de letras usando `input()`
- Revelar na tela todas as posições da palavra correspondentes à letra informada
- Rastrear o número de tentativas incorretas restantes

### 🛠️ Fim de Jogo

#### Descrição
Defina quando o jogo termina e informe o resultado ao jogador.

#### Requisitos
O programa completo deve:

- Encerrar quando a palavra for adivinhada completamente ou quando as tentativas se esgotarem
- Exibir uma mensagem de vitória ou de derrota ao final da partida