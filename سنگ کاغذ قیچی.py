
print("\n WELCOME TO THE GAME!!!!")

Player_1 = input("\n Player_1 , please enter your choice :").lower().strip()
Player_2 = input("\n player_2 , please enter your choice :").lower().strip()

if Player_1 == "scissors" and Player_2 == "paper":
    print("\n Pleyer_1 winnnnn!!!")
elif Player_1 == "paper" and Player_2 == "rock":
    print("\n Pleyer_1 winnnnn!!!")
elif Player_1 == "rock" and Player_2 == "scissors":
    print("\n player_1 winnnnn!!!")
elif Player_1 == "paper" and Player_2 == "scissors":
    print("\n Pleyer_2 winnnnn!!!")
elif Player_1 == "rock" and Player_2 == "paper":
    print("\n Pleyer_2 winnnnn!!!")
elif Player_1 == "scissors" and Player_2 == "rock":
    print("\n player_2 winnnnn!!!")
elif Player_1 == Player_2:
    print("\n Draw")
else:
    print("\n Please write the correct word.")   



