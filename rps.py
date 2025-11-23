'''
1 for Rock
0 for Paper
-1 for Scissor
'''
import random

you_Dict = { "r":1, "R":1 , "p":0 , "P":0, "s":-1 ,"S":-1}
reverse_Dict = { 1:"Rock" , 0:"Paper" , -1:"Scissor"}

user_score = 0
comp_score = 0

while True:
    you_str = input("\nEnter your choice (R/P/S) or Q to quit: ")

    if you_str.lower() == "q":
        print("\nGame Ended!")
        break

    if you_str not in you_Dict:
        print("Invalid input! Please enter R, P, S, or Q.")
        continue

    you_Choice = you_Dict[you_str]
    comp_choice = random.choice([-1 , 0 , 1])

    print(f"\nYou Chose: {reverse_Dict[you_Choice]}")
    print(f"Computer Chose: {reverse_Dict[comp_choice]}")

    if comp_choice == you_Choice:
        print("It's a Draw!")

    else:
        if(comp_choice == -1 and you_Choice == 1): 
            print("You Win! :)")
            user_score += 1

        elif(comp_choice == -1 and you_Choice == 0):
            print("You Lose! :(")
            comp_score += 1

        elif(comp_choice == 1 and you_Choice == -1):
            print("You Lose! :(")
            comp_score += 1

        elif(comp_choice == 1 and you_Choice == 0):
            print("You Win! :)")
            user_score += 1

        elif(comp_choice == 0 and you_Choice == -1):
            print("You Win! :)")
            user_score += 1

        elif(comp_choice == 0 and you_Choice == 1):
            print("You Lose! :(")
            comp_score += 1

        else:
            print("Something went wrong!")

# After loop ends
print("\n========== FINAL SCORE ==========")
print(f"Your Score: {user_score}")
print(f"Computer Score: {comp_score}")

if user_score > comp_score:
    print("🎉 You Won the Game Overall!")
elif comp_score > user_score:
    print("😢 Computer Won the Game!")
else:
    print("🤝 It's a Draw !")
print("=================================\n")
