# Snake Game (Jogo da Cobrinha)

Este é um projeto de um jogo da cobrinha (Snake Game) desenvolvido em Python, utilizando o padrão MVC (Model-View-Controller). O objetivo do jogo é controlar a cobrinha, comer a comida que aparece na tela e crescer o máximo possível sem colidir com as paredes ou com o próprio corpo.

## Estrutura do Projeto

```
cobrinha.py                # Arquivo principal para iniciar o jogo
controller/
  game_controller.py       # Lógica de controle do jogo
model/
  snake.py                # Lógica da cobrinha
  food.py                 # Lógica da comida
view/
  view.py                 # Interface gráfica do jogo
```

## Como Executar

1. **Pré-requisitos:**
   - Python 3.10 ou superior instalado
   - (Opcional) Recomenda-se o uso de um ambiente virtual

2. **Clone o repositório:**
   ```bash
   git clone https://github.com/devjogerio/snake_game.git
   cd snake_game
   ```

3. **Instale as dependências:**
   - Se houver dependências, instale com:
     ```bash
     pip install -r requirements.txt
     ```
   - Caso não exista o arquivo `requirements.txt`, o projeto pode não ter dependências externas além da biblioteca padrão do Python.

4. **Execute o jogo:**
   ```bash
   python cobrinha.py
   ```

## Funcionalidades
- Controle da cobrinha pelo teclado
- Geração aleatória de comida
- Crescimento da cobrinha ao comer
- Detecção de colisão com paredes e com o próprio corpo
- Interface gráfica simples

## Padrão de Projeto
O projeto segue o padrão MVC:
- **Model:** Representa os dados e regras de negócio (`model/snake.py`, `model/food.py`)
- **View:** Responsável pela interface gráfica (`view/view.py`)
- **Controller:** Gerencia a lógica do jogo e a comunicação entre Model e View (`controller/game_controller.py`)

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
Desenvolvido por devjogerio
