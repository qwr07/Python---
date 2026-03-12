import random
choices =["rock","paper","scissors"]
player_score =0
computer_score=0
while True:
    player=input("choice: rock, paper, scissors or exit:").lower()
    if player=="exit":
        print("Game over")
        print("your score",player_score)
        print("computer score",computer_score)
        break
    if player not in choices:
        print("invalid choice")
        continue
    computer=random.choice(choices)
    print("computer choice:",computer)
    if player==computer:
        print("it's a tie!")
    elif(player=="rock"and computer=="scisssors") or \
        (player=="paper"and computer=="rock")or\
        (player=="scissors"and computer=="paper"):
        print("you win this round!")
        player_score+=1
    else:
        print("computer win this round!")
        computer_score+=1
    print("score-you:",player_score,"computer:",computer_score)
