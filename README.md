# 🎮 Terminal Tic-Tac-Toe (Human vs AI)

A terminal-based Tic-Tac-Toe game where you play against an unbeatable AI using the **Minimax algorithm**.  
Features a 3×3 grid, simple input, win/draw detection, and smart AI moves.  
Perfect for learning basic Python and game AI.

---

## 🧱 Features

- 🤖 AI uses Minimax (never loses)
- 👤 Human vs AI gameplay
- 🎯 Clean 3×3 grid and terminal UI
- ✅ Win, draw, and move validation
- 🐍 100% Python-based, no extra libraries

---

## 🚀 How to Run

1. Save the code as `tic_tac_toe.py`.
2. Open your terminal and run:

```bash
python tic_tac_toe.py
```

---

## 🎮 How to Play

- You'll be asked to choose **X** or **O**.
- Input your move as `row column` (e.g., `1 1` for top-left).
- The AI will respond after each of your moves.
- The game ends when someone wins or it's a draw.

---

## 💡 Example (AI Forces a Draw)

```
Do you want to play as X or O? X
You are X, I am O.

Current board:
   |   |  
---------
   |   |  
---------
   |   |  

Enter your move (row column): 1 1
You played at (1, 1)
I play at (2, 2)

Current board:
 X |   |  
---------
   | O |  
---------
   |   |  

Enter your move (row column): 1 3
You played at (1, 3)
I play at (1, 2)

Current board:
 X | O | X
---------
   | O |  
---------
   |   |  

Enter your move (row column): 2 1
You played at (2, 1)
I play at (3, 1)

Current board:
 X | O | X
---------
 X | O |  
---------
 O |   |  

Enter your move (row column): 2 3
You played at (2, 3)
I play at (3, 2)

Current board:
 X | O | X
---------
 X | O | X
---------
 O | O |  

Enter your move (row column): 3 3
You played at (3, 3)

It's a draw!

Final board:
 X | O | X
---------
 X | O | X
---------
 O | O | X
```

---

## 🧩 Learning Highlights

- Minimax Algorithm  
- Recursion and Backtracking  
- Turn-based game logic  
- Python input handling and loops

---

Enjoy the game and feel free to improve it! 
