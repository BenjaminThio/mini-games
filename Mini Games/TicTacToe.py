import os

gameOver = False
player = False
sign = ["❌", "⭕️"]
board = ["⬜️" for i in range(9)]

def Render():
    renderer = ""
    counter = 0
    for i in range(9):
        renderer += board[i]
        counter += 1
        if counter == 3:
            renderer += "\n"
            counter = 0
    return renderer

def Win():
    winCases = [
        [0, 1, 2],
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 4, 8], 
        [2, 4, 6]
    ]
    for winCase in winCases:
        if board[winCase[0]] == board[winCase[1]] == board[winCase[2]] == sign[int(player)]:
            return True
    return False

os.system('clear||cls')

while not gameOver:
    position = input("Pls type a number between 1 - 9: ")
    if position.isdigit() and int(position) >= 1 and int(position) <= 9:
        board[int(position) - 1] = sign[int(player)]
        os.system('clear||cls')
        print(Render())
    else:
        continue
    if Win():
        print(f"Game Over! Player {int(player) + 1} won!")
        gameOver = True
    elif "⬜️" not in board:
        print("Game Over! It was a tie!")
        gameOver = True
    player = not player

"""
Coding The Shortest Tic Tac Toe Game Challenge
GameOver = False
Player = False
Board = ["🟡" for i in range(9)]
Symbol = ["❌", "⭕️"]

while not GameOver:
	Position = input("Please type a number between 1-9: ")
	if Position.isdigit() and int(Position) > 0 and int(Position) <= 10:
		Board[int(Position) - 1] = Symbol[int(Player)]
		print(f"{Board[0]}{Board[1]}{Board[2]}\n{Board[3]}{Board[4]}{Board[5]}\n{Board[6]}{Board[7]}{Board[8]}")
	else: continue
	if Board[0] == Board[1] == Board[2] == Symbol[int(Player)] or Board[3] == Board[4] == Board[5] == Symbol[int(Player)] or Board[6] == Board[7] == Board[8] == Symbol[int(Player)] or Board[0] == Board[3] == Board[6] == Symbol[int(Player)] or Board[1] == Board[4] == Board[7] == Symbol[int(Player)] or Board[2] == Board[5] == Board[8] == Symbol[int(Player)] or Board[0] == Board[4] == Board[8] == Symbol[int(Player)] or Board[2] == Board[4] == Board[6] == Symbol[int(Player)]:
		print(f"Game Over! Player {int(Player) + 1} wins!")
		GameOver = True
	elif "🟡" not in Board:
		print("Game Over! It was a tie!")
		GameOver = True
	Player = not Player
"""