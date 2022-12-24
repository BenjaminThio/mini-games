import threading
import keyboard
import random
import time
import os

speed = 10
height = 10
length = 10
background = '⬜️'
barrier = '🟦'
food = '🍎'
snakeHead = '🤢'
snakeBody = '🟢'

gameOver = False
world = [[background for _ in range(length)] for _ in range(height)]
snakeCoords = [random.choice([[x, y] for x in range(height) for y in range(length)])]
snakeDirection = 'right'
foodCoord = None
score = 9
alphaKeys = ['w', 'a', 's', 'd']
arrowKeys = ['up', 'left', 'down', 'right']
keys = alphaKeys + arrowKeys
directions = dict(zip(alphaKeys, arrowKeys))

def Render():
    global world
    counter = 0
    renderer = ''
    world = [[background for _ in range(length)] for _ in range(height)]
    if foodCoord != None:
        world[foodCoord[1]][foodCoord[0]] = food
    for coord in snakeCoords:
        if counter == 0:
            world[coord[1]][coord[0]] = snakeHead
        else:
            world[coord[1]][coord[0]] = snakeBody
        counter += 1
    renderer += f'{barrier * (length + 2)}\n{barrier}'
    renderer += barrier.join([f"{''.join([world[y][x] for x in range(len(world[y]))])}{barrier}\n" for y in range(len(world))])    
    renderer += f'{barrier * (length + 2)}'
    print(renderer)

def UpdateSnakeMovement():
    global foodCoord
    global gameOver
    global score
    if snakeDirection == 'up':
        if snakeCoords[0][1] - 1 >= 0:
            snakeCoords.insert(0, [snakeCoords[0][0], snakeCoords[0][1] - 1])
        else:
            snakeCoords.insert(0, [snakeCoords[0][0], height - 1])
    elif snakeDirection == 'left':
        if snakeCoords[0][0] - 1 >= 0:
            snakeCoords.insert(0, [snakeCoords[0][0] - 1, snakeCoords[0][1]])
        else:
            snakeCoords.insert(0, [length - 1, snakeCoords[0][1]])
    elif snakeDirection == 'down':
        if snakeCoords[0][1] + 1 <= height - 1:
            snakeCoords.insert(0, [snakeCoords[0][0], snakeCoords[0][1] + 1])
        else:
            snakeCoords.insert(0, [snakeCoords[0][0], 0])
    elif snakeDirection == 'right':
        if snakeCoords[0][0] + 1 <= length - 1:
            snakeCoords.insert(0, [snakeCoords[0][0] + 1, snakeCoords[0][1]])
        else:
            snakeCoords.insert(0, [0, snakeCoords[0][1]])
    if snakeCoords[0] in [snakeCoords[i] for i in range(1, len(snakeCoords))]:
        gameOver = True
    if snakeCoords[0] == foodCoord:
        score += 1
        foodCoord = None
        return
    snakeCoords.pop(-1)

def ChangeDirection():
    global snakeDirection
    while not gameOver:
        for key in keys:
            if keyboard.is_pressed(key):
                if key in alphaKeys:
                    key = directions[key]
                if len(snakeCoords) > 1:
                    if key == 'up' and snakeDirection == 'down' or key == 'down' and snakeDirection == 'up' or key == 'left' and snakeDirection == 'right' or key == 'right' and snakeDirection == 'left':
                        continue
                snakeDirection = key
                break

def GenerateFood():
    global foodCoord
    global gameOver
    if foodCoord == None:
        availableCoords = [[x, y] for x in range(length) for y in range(height) if [x, y] not in snakeCoords]
        if len(availableCoords) > 0:
            randomCoord = random.choice(availableCoords)
            foodCoord = [randomCoord[0], randomCoord[1]]
        else:
            gameOver = True

if __name__ == "__main__":
    threading.Thread(target=ChangeDirection, daemon=True).start()

    while not gameOver:
        time.sleep(speed ** -1)
        os.system('cls||clear')
        GenerateFood()
        Render()
        UpdateSnakeMovement()

    if score == length * height:
        print('You Win!!!')
    else:
        print('Game Over!')
    print(f'Score: {score}')