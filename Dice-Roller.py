import random
def roll_dice():
    return random.randint(1,6)
#Ask user for input
while True:
   user_input= input("\n Roll a dice? (yes or no):\n")
   if user_input== "yes":
      result= roll_dice()
      print(f"You rolled a {result}")

   elif user_input== "no":
      print("BYE!")
      break 

   else:
    print("Enter yes or no")
    continue
