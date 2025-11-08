
### Select Your Language / Selecione seu Idioma
[![English](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/50px-Flag_of_the_United_Kingdom_%283-5%29.svg.png)](#-english-instructions)  
[![Português](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/45px-Flag_of_Brazil.svg.png)](#-instruções-em-português)


## 🇬🇧 English Instructions

### 🚀 Overview
**NanoVirus Outbreak** is a 2D platformer where you control a micro robot injected into the human body to eliminate a viral infection. Collect all energy fruits and avoid the deadly viruses!

**Platform:** Pygame Zero  
**Genre:** 2D Platformer  
**Resolution:** 800×480 px  
**Project Type:** Educational Project for Python Tutor Position

### 🎯 Project Requirements Met
- ✅ Uses only allowed modules: `pgzero`, `math`, `random`, and `Rect` from Pygame
- ✅ Platformer game with smooth character movement and animations
- ✅ Main menu with clickable buttons
- ✅ Background music and sound effects with toggle option
- ✅ Animated enemies with defined movement patterns
- ✅ Sprite animations for all characters
- ✅ Clean, PEP8-compliant code
- ✅ Unique and original implementation

### 🎯 Objective
- Collect all **energy fruits** (8 in total)
- Avoid contact with the **viruses** patrolling the area
- Survive with your **3 health points**
- Defeat the infection!

### 🎮 Controls
| Key | Action |
|-----|--------|
| **← →** | Move left/right |
| **SPACE** or **↑** | Jump |
| **Mouse** | Click menu buttons |

### ⚙️ Game Mechanics

#### 🤖 Player (Micro Robot)
- **HP:** 3 hearts
- **Movement:** Walk and jump with gravity physics
- **Damage:** Flashes red when hit
- **Temporary invincibility:** 1 second after taking damage

#### 🦠 Viruses (Enemies)
- Move horizontally in defined patterns
- Cause **1 damage** on player contact
- Rotating spike animation
- 3 viruses scattered through the level

#### 🍓 Energy Fruits
- **8 fruits** to collect
- Floating animation
- Collection sound when picked up
- Victory when all are collected

### 📋 Game States
1. **Main Menu**
   - Start Game
   - Toggle Sound (ON/OFF)
   - Exit

2. **Playing**
   - Main platforming level
   - HUD showing HP and collected fruits

3. **Game Over**
   - Appears when HP reaches zero
   - Press SPACE to return to menu

4. **Victory**
   - Appears when all fruits are collected
   - Press SPACE to return to menu

### 🎨 Visual Design
- **Background:** Dark red (simulating inside the body)
- **Player:** Cyan robot with animated eyes
- **Viruses:** Green spheres with spikes
- **Fruits:** Red strawberries with green leaves
- **UI:** Hearts for HP, fruit counter

### 🔊 Sound System
The game features an integrated sound system (can be toggled):
- **Background music** on loop
- **Jump sound**
- **Fruit collection** sound
- **Damage** sound when hit

*Note: Sound files must be in the `sounds/` folder to work.*

### 🚀 How to Run

#### Requirements
```bash
pip install -r requirements.txt
```

#### Run the game
```bash
python game_pgzero.py
```

or

```bash
pgzrun game_pgzero.py
```

## 🇧🇷 Instruções em Português

### 🚀 Visão Geral
**NanoVirus Outbreak** é um jogo de plataforma 2D onde você controla um microrrobô injetado no corpo humano para eliminar uma infecção viral. Colete todas as frutas de energia e evite os vírus mortais!

**Plataforma:** Pygame Zero  
**Gênero:** Plataforma 2D  
**Resolução:** 800×480 px

### 🎯 Objetivo
- Coletar todas as **frutas de energia** (8 no total)
- Evitar contato com os **vírus** que patrulham a área
- Sobreviver com seus **3 pontos de vida**
- Vencer a infecção!

### 🕹️ Controles
| Tecla | Ação |
|-------|------|
| **← →** | Mover esquerda/direita |
| **ESPAÇO** ou **↑** | Pular |
| **Mouse** | Clicar nos botões do menu |

### ⚙️ Mecânicas do Jogo

#### 🤖 Jogador (Microrrobô)
- **HP:** 3 corações
- **Movimento:** Andar e pular com física de gravidade
- **Dano:** Pisca em vermelho ao ser atingido
- **Invencibilidade temporária:** 1 segundo após levar dano

#### 🦠 Vírus (Inimigos)
- Movem-se horizontalmente em padrões definidos
- Causam **1 de dano** ao tocar o jogador
- Animação de espinhos rotativos
- 3 vírus espalhados pela fase

#### 🍓 Frutas de Energia
- **8 frutas** para coletar
- Animação flutuante
- Som de coleta ao pegar
- Vitória ao coletar todas

### 📋 Estados do Jogo
1. **Menu Principal**
   - Iniciar Jogo
   - Alternar Som (LIGAR/DESLIGAR)
   - Sair

2. **Jogando**
   - Fase principal com plataforma
   - HUD mostrando HP e frutas coletadas

3. **Game Over**
   - Aparece ao perder todos os HP
   - Pressione ESPAÇO para voltar ao menu

4. **Vitória**
   - Aparece ao coletar todas as frutas
   - Pressione ESPAÇO para voltar ao menu

### 🎨 Design Visual
- **Fundo:** Vermelho escuro (simulando interior do corpo)
- **Jogador:** Robô ciano com olhos animados
- **Vírus:** Esferas verdes com espinhos
- **Frutas:** Morangos vermelhos com folha verde
- **UI:** Corações para HP, contador de frutas

### 🔊 Sistema de Som
O jogo possui sistema de som integrado (pode ser ativado/desativado):
- **Música de fundo** em loop
- **Som de pulo**
- **Som de coleta** de frutas
- **Som de dano** ao ser atingido

*Nota: Os arquivos de som devem estar na pasta `sounds/` para funcionar.*

### 🚀 Como Executar

#### Requisitos
```bash
pip install -r requirements.txt
```

#### Executar o jogo
```bash
python game_pgzero.py
```

ou

```bash
pgzrun game_pgzero.py
```

## 🛠️ Tecnologias Utilizadas / Technologies Used

**Linguagem/Language:** Python 3  
**Framework:** Pygame Zero
```
📁 project/
├── game_pgzero.py    # Arquivo principal do jogo / Main game file
├── requirements.txt  # Dependências / Dependencies
├── images/           # Pasta para imagens / Images folder
│   ├── player/       # Sprites do jogador / Player sprites
│   ├── virus/        # Sprites dos vírus / Virus sprites
│   └── fruits/       # Sprites das frutas / Fruit sprites
└── sounds/           # Pasta para áudio / Audio folder (optional)
    ├── back.ogg      # Música de fundo / Background music
    ├── jump.ogg      # Som de pulo / Jump sound
    ├── collect.ogg   # Som de coleta / Collect sound
    └── hit.ogg       # Som de dano / Damage sound
```

## 🧩 Estrutura do Código / Code Structure

### Classes Principais / Main Classes
- **Player**: Controla o personagem principal / Controls the main character
- **Virus**: Inimigos que patrulham a fase / Enemies that patrol the level
- **Fruit**: Itens colecionáveis para pontuação / Collectible items for scoring
- **Platform**: Plataformas onde o jogador pode pisar / Platforms the player can stand on
- **Button**: Botões para o menu / Buttons for the menu interface

- **`Player`**: Controla o robô jogador
  - Física de movimento e gravidade
  - Sistema de HP e dano
  - Animações e estados

- **`Virus`**: Inimigos que patrulham
  - Movimento horizontal com limites
  - Detecção de colisão
  - Animação de espinhos

- **`Fruit`**: Coletáveis de energia
  - Animação flutuante
  - Sistema de coleta
  - Contador de score

- **`Button`**: Botões do menu
  - Detecção de hover
  - Sistema de cliques
  - Visual interativo

### Funções Principais

- `update()`: Loop principal de atualização
- `draw()`: Renderização de todos os elementos
- `init_menu()`: Inicializa o menu
- `init_game()`: Configura a fase
- `on_mouse_down()`: Gerencia cliques
- `on_key_down()`: Gerencia teclas

## 🎓 Conceitos Aplicados

✅ **Programação Orientada a Objetos**  
✅ **Física de jogo** (gravidade, colisão)  
✅ **Sistema de estados** (menu, jogo, game over)  
✅ **Animações** procedurais  
✅ **Interface de usuário** interativa  
✅ **Sistema de pontuação**  
✅ **Gerenciamento de som**  
✅ **Código limpo** seguindo PEP8  

## 🎮 Dicas de Jogo

1. **Timing é tudo**: Espere os vírus se afastarem antes de passar
2. **Pule com cuidado**: Você não pode pular no ar
3. **Invencibilidade**: Use o tempo de invencibilidade após levar dano
4. **Explore**: Algumas frutas estão em posições mais altas
8. **Não tenha pressa**: Observe os padrões dos vírus

## 🔧 Personalização

Você pode facilmente modificar:

- **Dificuldade**: Ajuste `PLAYER_SPEED`, `GRAVITY`, `JUMP_STRENGTH`
- **HP do jogador**: Modifique `self.max_hp` na classe `Player`
- **Número de inimigos**: Adicione mais vírus em `init_game()`
- **Quantidade de frutas**: Adicione mais frutas na lista
- **Cores**: Altere as cores em cada função `draw()`

## 📝 Código Original

Este jogo foi desenvolvido 100% do zero, sem uso de templates ou código de terceiros. Todas as mecânicas, classes e funções foram criadas especificamente para este projeto.

**Total de linhas:** ~488 linhas  
**Padrão de código:** PEP8  
**Linguagem:** Python 3  
**Framework:** Pygame Zero  

## 🏆 Créditos / Credits

### Desenvolvido por / Developed by
- [Gean / Gean]

### Recursos / Assets
- Músicas e efeitos sonoros: [Uso livre / Free use]
- Sprites e arte: [Uso livre / Free use]




## 🤝 Contribuição / Contributing

Este projeto foi desenvolvido como parte de um teste para tutoria de Python. Contribuições não são esperadas, mas feedback é sempre bem-vindo!

This project was developed as part of a Python tutoring test. While contributions aren't expected, feedback is always welcome!

## 📈 Divirta-se eliminando vírus! / Have fun eliminating viruses!
