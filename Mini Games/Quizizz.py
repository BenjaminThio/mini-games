import string
import random
import os
import asyncio

GameOver = False
Alphabet = list(string.ascii_lowercase)
Score = 0
Quests = [
    {"Question": "Which of the following is MOST reactive?", "Options": ["Magnesium", "Lead", "Tin", "Copper", "Zinc"], "Answer": 0}, 
    {"Question": "Which metal is more reactive than calcium?", "Options": ["Magnesium", "potassium", "silver", "aluminum"], "Answer": 1}, 
    {"Question": "How can you tell that a metal is reacting with water?", "Options": ["Colour change", "Bright light", "Fizzing", "It gets colder"], "Answer": 2},
    {"Question": "Choose the least reactive metal", "Options": ["calcium", "magnesium", "iron", "copper"], "Answer": 3},
    {"Question": "Choose the most reactive metal", "Options": ["calcium", "magnesium", "iron", "copper"], "Answer": 0}
]
QuestSum = len(Quests)
Count = 1
Quest = None
Loop = asyncio.get_event_loop()

async def Preview(Message, Length):
    def Render(Countdown):
        os.system("cls||clear")
        print(Message)
        print(f"Preview countdowm in {Length - Countdown}")
        print(f"[{''.join(Progress)}]")
    Progress = ["🟥" for i in range(Length)]
    Render(0)
    for i in range(1, Length + 1):
        Progress[i - 1] = "🟩"
        await asyncio.sleep(1)
        Render(i)
    await asyncio.sleep(1)

while not GameOver:
    if len(Quests) > 0:
        os.system("cls||clear")
        if Quest == None: Quest = random.choice(range(len(Quests)))
        print(f"Question {Count}: {Quests[Quest]['Question']}\n" + '\n'.join([f'({Alphabet[i]}) {Quests[Quest]["Options"][i]}' for i in range(len(Quests[Quest]['Options']))]))
        Input = input(f"Please type a answer between {', '.join([Alphabet[i] for i in range(len(Quests[Quest]['Options']))])}: ")
        if Input.lower() in [Alphabet[i] for i in range(len(Quests[Quest]['Options']))]:
            if Input.lower() == Alphabet[Quests[Quest]["Answer"]]:
                Loop.run_until_complete(Preview("You are right!", 3))
                Score += 1
            else:
                Loop.run_until_complete(Preview(f"You are wrong! Answer is `{Alphabet[Quests[Quest]['Answer']].upper()}`", 10))
            Quests.pop(Quest)
            Quest = None
            Count += 1
            continue
        else:
            Loop.run_until_complete(Preview("Please try again!", 3))
            continue
    else:
        os.system("cls||clear")
        print(f"GameOver! Your score is {Score / QuestSum * 100}%")
        GameOver = True