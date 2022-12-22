import requests
import random
import asyncio
import os

progress = [
"""
┳━━━━━━━━━━┓
┃         🏮
┃         /|\\
┃
┃
┃
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃         🏮
┃         /|\\
┃
┃
┃
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃         /|\\
┃
┃
┃
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃
┃
┃
┃
┃
┃
"""
,

"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃   🎩
┃
┃
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃   👔
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃  /👔
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃  /👔\\
┃
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃  /👔\\
┃   👖
┃
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃  /👔\\
┃   👖
┃  /
┃
"""
,
"""
┳━━━━┿━━━━━┓
┃    │    🏮
┃    │    /|\\
┃  ╭🎩╮
┃  ╰👴╯
┃  /👔\\
┃   👖
┃  /  \\
┃
"""
]
gameOver = False
site = "https://www.mit.edu/~ecprice/wordlist.10000"
Response = requests.get(site)
words = [i for i in Response.content.decode().split("\n") if len(i) >= 5]

Loop = asyncio.get_event_loop()

async def Preview(Text, Length):
    def Render(Countdown):
        os.system("cls||clear")
        print(f"{Text}\n\nPreview countdown in {Length - Countdown}\n[{''.join(Progress)}]")
    Progress = ["🟥" for i in range(Length)]
    Render(0)
    for i in range(1, Length + 1):
        Progress[i - 1] = "🟩"
        await asyncio.sleep(1)
        Render(i)
    await asyncio.sleep(1)
    os.system("cls||clear")

while not gameOver:
    word = random.choice(words).lower()
    guess = []
    Counter = 0
    os.system("cls||clear")
    start = input("Do you want to play Hangman game?\nPlease enter y(yes) or n(no): ")
    while start != "y" and start != "n":
        start = input("Do you want to play Hangman game?\nPlease enter y(yes) or n(no): ")
    if start == "n":
        break
    while not gameOver:
        os.system("cls||clear")
        Counter += 1
        if Counter >= len(progress):
            print(progress[Counter - 1].strip())
            Loop.run_until_complete(Preview(f"Game over! You died! The word is `{word}`", 10))
            break
        print(progress[Counter - 1].strip())
        key = ["_" for i in range(len(word))]
        for i in range(len(word)):
            if list(word)[i] in guess:
                key[i] = list(word)[i]
        if "_" not in key:
            print(" ".join(key))
            Loop.run_until_complete(Preview("You won the game!", 5))
            break
        print(" ".join(key))
        userInput = input("Please enter a letter: ").lower()
        if userInput.isalpha() and len(userInput) == 1 and userInput in word:
            if userInput not in guess:
                guess.append(userInput)
                if Counter > 0:
                    Counter -= 1
        continue
os.system("cls||clear")