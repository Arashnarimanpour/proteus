
print("\n WELCOME TO THE GAME!!!!")

#محل وارد کردن(ورودی) انتخاب هر بازیکن
Player_1 = input("\n Player_1 , please enter your choice :").lower()
Player_2 = input("\n player_2 , please enter your choice :").lower()

#در صورتی که بازیکن اول قیچی و بازیکن دوم کاغذ باشه 
if Player_1 == "scissors" and Player_2 == "paper" :
 #در خروجی بازیکن اول برنده است
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
#در صورتی که انتخاب بازکن ها یکسان باشد
elif Player_1 == Player_2:
    print("\n Draw")
#در صورتی که هر چیزی بجز سنگ و کاغذ و قیچی وارد شود
else:
    print("\n Please write the correct word.")   



