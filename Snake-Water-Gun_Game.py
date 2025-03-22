import random
choices = {1: "Snake 🐍", 2: "Gun 🔫", 3: "Water 💧"}
while True:
    player = int(input("Enter 1(Snake)/2(Gun)/3(Water) : "))
    if player in choices:
        break
    else:
        print("Inavalid choice!, Please enter 1/2/3")
computer = random.randint(1,3)
print(f"You choose - {choices[player]} ")
print(f"Computer choose - {choices[computer]}")
if (player==1 and computer==3):
    print ("Snake 🐍 drinks Water 💧 \nYou Win!🎉")
elif (player==3 and computer==2):
    print ("Water 💧 douses Gun 🔫 \nYou Win!🎉")
elif (player==2 and computer==1):
    print ("Gun 🔫 kills Snake 🐍 \nYou Win!🎉")
elif (player==computer):
   print("Match Draw!🤝")
else :
    print("You Loose!😔")
    
print("Thankyou for playing this game!🎮\nVisit Again!")
  

    