
# Snake Game (Jogo da Cobrinha)

<p align="center">
  <img src="https://raw.githubusercontent.com/devjogerio/snake_game/master/.github/snake_game_demo.gif" alt="Demonstração do Jogo da Cobrinha" width="400"/>
</p>

<p align="center">
  <a href="https://github.com/devjogerio/snake_game"><img src="https://img.shields.io/github/license/devjogerio/snake_game?style=flat-square" alt="License"></a>
  <a href="https://github.com/devjogerio/snake_game/stargazers"><img src="https://img.shields.io/github/stars/devjogerio/snake_game?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/devjogerio/snake_game/commits/master"><img src="https://img.shields.io/github/last-commit/devjogerio/snake_game?style=flat-square" alt="Last Commit"></a>
</p>

Este é um projeto de um jogo da cobrinha (Snake Game) desenvolvido em Python, utilizando o padrão MVC (Model-View-Controller). O objetivo do jogo é controlar a cobrinha, comer a comida que aparece na tela e crescer o máximo possível sem colidir com as paredes ou com o próprio corpo.

## Demonstração

<p align="center">
  <img src="https://raw.githubusercontent.com/devjogerio/snake_game/master/.github/snake_game_screenshot.png" alt="Screenshot do Jogo" width="400"/>
</p>


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
- Pontuação exibida em tempo real
- Código organizado e comentado


## Padrão de Projeto
O projeto segue o padrão MVC:
- **Model:** Representa os dados e regras de negócio (`model/snake.py`, `model/food.py`)
- **View:** Responsável pela interface gráfica (`view/view.py`)
- **Controller:** Gerencia a lógica do jogo e a comunicação entre Model e View (`controller/game_controller.py`)


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Minha nova feature'`)
4. Push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request


## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
Desenvolvido por devjogerio
