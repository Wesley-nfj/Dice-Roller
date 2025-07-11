import random
from collections import defaultdict

def roll_dice():
    return random.randint(1,6)

roll_count= defaultdict(int)
total_roll =0
#Ask user for input
while True:
   user_input= input("\n Roll a dice? (yes or no):\n")
   if user_input== "yes":
      result= roll_dice()
      roll_count[result] += 1
      total_roll +=1
      print(f"You rolled a {result}")

   elif user_input== "no":
       print("\n🎯 Roll Summary:")
       print(f"Total rolls: {total_rolls}")
       for face in range(1, 7):
           count = roll_counts[face]
           print(f"Face {face}: {count}")
      print("BYE!")
      break 

   else:
    print("Enter yes or no")
    continue
