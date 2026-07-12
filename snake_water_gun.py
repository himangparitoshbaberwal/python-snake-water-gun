# help to choose random choice
import random
# help to give voice feedback
import pyttsx3
# initialise voice function and give voice command
def speak(message):
    print(message)
    engine=pyttsx3.init()           # Initializing the engine inside the function because, on my Python setup,
    engine.say(message)             # reusing a single engine only speaks once.
    engine.runAndWait()
win_count = 0
lose_count = 0
draw_count = 0
# main program which contain game logic
def play_game():
    global win_count, lose_count, draw_count
    computer={-1:"snake",0:"water",1:"gun"}
    user={"s":"snake","w":"water","g":"gun"}
    computer_move=random.choice([-1,1,0])
    user_choice=input("enter your choice as s for snake,w for water and g for gun:")
    if user_choice not in user:
        print("Please enter only s, w or g.")
        return
    elif(user[user_choice]==computer[computer_move]):
        message="same so no one won"
        speak(message)
        draw_count+=1
    elif(user[user_choice]=="snake" and computer[computer_move]=="water"):
        message="computer chose water, so you win"
        speak(message)
        win_count+=1
    elif(user[user_choice]=="snake" and computer[computer_move]=="gun"):
        message="computer chose gun, so you lose"
        speak(message)
        lose_count+=1
    elif(user[user_choice]=="water" and computer[computer_move]=="snake"):
        message="computer chose snake, so you lose"
        speak(message)
        lose_count+=1
    elif(user[user_choice]=="water" and computer[computer_move]=="gun"):
        message="computer chose gun, so you win"
        speak(message)
        win_count+=1
    elif(user[user_choice]=="gun" and computer[computer_move]=="snake"):
        message="computer chose snake, so you win"
        speak(message)
        win_count+=1
    elif(user[user_choice]=="gun" and computer[computer_move]=="water"):
        message="computer chose water, so you lose"
        speak(message)
        lose_count+=1
    else:
        print("Please give valid input")
# let player restart the game
def restart():
    rounds=int(input("enter number of rounds you want to play: "))
    if(rounds<1):
        print("Please enter a positive number of rounds.")
        return
    for i in range(1,rounds+1):
        play_game()
p=input("Do you want to play the game: ")
if(p.lower()=="yes"):
    restart()
elif(p.lower()=="no"):
    print("Ok you can try next time")
else:
    print("please chose yes or no")
while True:
    r=input("Do you want to restart the game: ")
    if r.lower()=="yes":
        restart()
    elif r.lower()=="no":
        print("\nThanks for playing! Godbye! 👋")
        break
    else:
        print("please tell yes or no")
print("=" * 55)
print("Final Score")
print(f"Wins   : {win_count}")
print(f"Losses : {lose_count}")
print(f"Draws  : {draw_count}")
print("=" * 55)