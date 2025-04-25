import random 
target = random.randint(1,100)
i = 1
while True:
    n = int (input("Enter the Number : "))
    if target > n :
        print("Higher Number Please!")
    elif target < n :
        print("Lower Number Please!")
    else :
        print("Congrats! You are Correct")
        break
    print("Choose once again!")
    i = i+1
if i <= 10:
    print (f"Impressive! You nailed the correct number in just {i} attempts!")
else :
    print(f"Not bad! You got the correct number in {i} tries.")
print("Well Played!")

