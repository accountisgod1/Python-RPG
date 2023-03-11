#Imports
import subprocess
import os
import time
import Settings as S
import Enemies as En
import PlayerStats as P
import random

#Main


SwordEquipped = False
SpearEquipped = False
ShieldEquipped = False

EquippedSword = {}
EquippedSpear = {}
EquippedShield = {}

os.makedirs("Achivements",exist_ok=True)

filepath = "C:/Users/User/Documents/RPG-GAME/Achivements"
filename = "Achivements.json"
filemain = os.path.join(filepath,filename)
towrite = """{"Achivements": "Active"}"""

with open(filemain,"w") as file:
   file.write(towrite)

print("Welcome To The Terminal RPG Game")
TutorialInput = input("To Fight Your First Enemy, Press A ")

if TutorialInput.lower() == "a":
    print("You Are Going To Fight A Goblin")
    print("Health: ",En.EnemiesStats["Goblin"]["Health"])
    print("Damage: ",En.EnemiesStats["Goblin"]["Damage"])
    AttackInput = input("What Do You Want To Attack With: ")
    if AttackInput.lower() == "punch":
        P.Stamina - S.Punch_Stamina
        print(f"Stamina: {P.Stamina}")
        En.EnemiesStats["Goblin"]["Health"] -=10
        print("Health:",En.EnemiesStats["Goblin"]["Health"])
        if En.EnemiesStats["Goblin"]["Health"] == 0:
           print("YOU WON!!")
           xp = 100
           print(xp)
           P.Coins += 100
           print("Coins:",P.Coins)

while P.Stamina < P.MaxStamina:
    P.Stamina += 1

#XP BLOCKS
if P.xp == 100:
    P.Level += 1
    print("Level UP! Level: ",P.Level)

elif P.xp >= 200:
    P.Level += 2
    print("Level UP! Level: ",P.Level)


TutorialInput = "Wow! You Defeated A Goblin!"
print(TutorialInput)

TutorialInput = input("Time To Go To The Village! Press V ")

if TutorialInput.lower() == "v":
    print("Loading Village")
    time.sleep(1)
    TutorialInput = input("W To Go The Weapon Shop, T For Training ")

    if TutorialInput.lower() == "w":
       print("This Place Has Every Sword, Spear, Shield In The World!")
       WeaponInput = input("S For Sword, SP For Spear, SH For Shield ")
       if WeaponInput.lower() == "s":
           SwordsList = ["Iron Sword","Diamond Sword","Wooden Sword","Ancient Sword","Gold Sword"]
           SpecialSwordList = ["Excalibur","Unknown Sword"]

           SwordsStats = {"Excalibur": {"Damage": 2500, "StaminaUsage": 90,"Price": 10000}, 
                    "Iron Sword": {"Damage": 50, "StaminaUsage": 10, "Price": 254},
                    "Unknown Sword": {"Damage": 500, "StaminaUsage": 67,"Price": 4700},
                    "Diamond Sword": {"Damage": 200, "StaminaUsage": 20,"Price": 1420},
                    "Wooden Sword": {"Damage": 21, "StaminaUsage": 6,"Price": 100},
                    "Ancient Sword": {"Damage": 1075,"StaminaUsage": 56,"Price": 4203},
                    "Gold Sword": {"Damage": 142, "StaminaUsage": 17, "Price": 1204}}

           SwordName = random.choice(SwordsList)

           SwordName1 = random.choice(SwordsList)

           if SwordName == SwordName1:
               SwordName1 = random.choice(SwordsList)

           if SwordName != "WoodenSword":
              SwordName = "Wooden Sword"

           InStock = [SwordName,SwordName1]

           DamageAmount = SwordsStats.get(SwordName).get("Damage")

           StaminaUsage = SwordsStats.get(SwordName).get("StaminaUsage")

           Price = SwordsStats.get(SwordName).get("Price")

           DamageAmount1 = SwordsStats.get(SwordName1).get("Damage")

           StaminaUsage1 = SwordsStats.get(SwordName1).get("StaminaUsage")

           Price1 = SwordsStats.get(SwordName1).get("Price")

           print(f"Swords In Stock: {InStock[0]}, {InStock[1]}")
           
           BuyInput = input("Pick Your Swords In Stock. ")

           if BuyInput == InStock[0]:
               print("You Are About To Buy: ",InStock[0])
               print(f"This Is The Stats, Damage: {DamageAmount} Stamina Usage:{StaminaUsage} Price: {Price} Coins")
               BuyInputCon = input("Do You Want To By This Sword? (Y/n) ")
               if BuyInputCon.lower() == "y":
                if P.Coins == Price:
                   InStock0 = True
                   SwordEquipped = True
                   EquippedSword = InStock[0]
                   print("Tutorial DONE!")
                   filepath = "C:/Users/User/Documents/RPG-GAME/Achivements"
                   filename = "TutorialCompleted.txt"
                   filemain = os.path.join(filepath,filename)
                   towrite = "Tutorial Completed"

                   with open(filemain,"w") as file:
                       file.write(towrite)

                elif P.Coins < Price:
                   print("You Don't Have Enough Coins")

           elif BuyInput == InStock[1]:
                print("You Are About To Buy: ",InStock[1])
                print(f"This Is The Stats, Damage: {DamageAmount1} ,Stamina Usage: {StaminaUsage1}, Price: {Price1} Coins")
                BuyInputCon = input("Do You Want To By This Sword? (Y/n) ")
                if BuyInputCon.lower() == "y":
                 if P.Coins == Price:
                   InStock1 = True
                   SwordEquipped = True
                   EquippedSword = InStock[1]
                   print("Tutorial DONE!")
                   filepath = "C:/Users/User/Documents/RPG-GAME/Achivements"
                   filename = "TutorialCompleted.txt"
                   filemain = os.path.join(filepath,filename)
                   towrite = "Tutorial Completed"

                   with open(filemain,"w") as file:
                       file.write(towrite)

                 elif P.Coins < Price:
                    print("You Don't Have Enough Coins")  
                   


                   

    elif TutorialInput.lower() == "t":
        TutorialInput = input("S To Increase Stamina ")
        if TutorialInput.lower() == "s":
            P.MaxStamina += 35
            print("Your Stamina Is: ",P.MaxStamina)


SelectionInput = input("V To Go To The Village, A To Attack")

if SelectionInput.lower() == "a":
   print("You Are Going To Fight A Skeleton Warrior")
   print("Health: ",En.EnemiesStats["Skeleton Warrior"]["Health"])
   print("Damage: ",En.EnemiesStats["Skeleton Warrior"]["Damage"])
   AttackInput = input("What Do You Want To Attack With: ")
   if AttackInput == "Punch":
       P.Stamina - S.Punch_Stamina
       print(f"Stamina: {P.Stamina}")
       En.EnemiesStats["Skeleton Warrior"]["Health"] -= 10
       En.EnemiesStats["Skeleton Warrior"]["Health"] += 0.5
       print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
       En.EnemiesStats["Skeleton Warrior"]["Health"] -= 10
       print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
       if En.EnemiesStats["Skeleton Warrior"]["Health"] == 0:
          print("YOU WON!!")
          xp = 100
          print(xp)
          P.Coins += 100
          print("Coins:",P.Coins)

   elif AttackInput == "Sword":
      if SwordEquipped == True:
          if InStock0 == True:
             P.Stamina -= StaminaUsage
             print(f"Stamina: {P.Stamina}")
             En.EnemiesStats["Skeleton Warrior"]["Health"] -= DamageAmount
             En.EnemiesStats["Skeleton Warrior"]["Health"] += 0.5
             print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
             En.EnemiesStats["Skeleton Warrior"]["Health"] -= DamageAmount
             print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
             if En.EnemiesStats["Skeleton Warrior"]["Health"] == 0:
                print("YOU WON!!")
                xp = 100
                print(xp)
                P.Coins += 100
                print("Coins:",P.Coins)

          elif InStock1 == True:
             P.Stamina -= StaminaUsage1
             print(f"Stamina: {P.Stamina}")
             En.EnemiesStats["Skeleton Warrior"]["Health"] -= DamageAmount1
             En.EnemiesStats["Skeleton Warrior"]["Health"] += 0.5
             print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
             En.EnemiesStats["Skeleton Warrior"]["Health"] -= DamageAmount
             print("Health:",En.EnemiesStats["Skeleton Warrior"]["Health"])
             if En.EnemiesStats["Skeleton Warrior"]["Health"] == 0:
                print("YOU WON!!")
                xp = 100
                print(xp)
                P.Coins += 100
                print("Coins:",P.Coins)

elif SelectionInput.lower() == "v":
    print("Loading Village")
    VillageInput = input("W To Go The Weapon Shop, T For Training ")

    if VillageInput.lower() == "w":
       print("This Place Has Every Sword, Spear, Shield In The World!")
       WeaponInput = input("S For Sword, SP For Spear, SH For Shield ")
       if WeaponInput.lower() == "s":
           SwordsList = ["Iron Sword","Diamond Sword","Wooden Sword","Ancient Sword","Gold Sword"]
           SpecialSwordList = ["Excalibur","Unknown Sword"]

           SwordsStats = {"Excalibur": {"Damage": 2500, "StaminaUsage": 90,"Price": 10000}, 
                    "Iron Sword": {"Damage": 50, "StaminaUsage": 10, "Price": 254},
                    "Unknown Sword": {"Damage": 500, "StaminaUsage": 67,"Price": 4700},
                    "Diamond Sword": {"Damage": 200, "StaminaUsage": 20,"Price": 1420},
                    "Wooden Sword": {"Damage": 21, "StaminaUsage": 6,"Price": 100},
                    "Ancient Sword": {"Damage": 1075,"StaminaUsage": 56,"Price": 4203},
                    "Gold Sword": {"Damage": 142, "StaminaUsage": 17, "Price": 1204}}

           SwordName = random.choice(SwordsList)

           SwordName1 = random.choice(SwordsList)

           if SwordName == SwordName1:
               SwordName1 = random.choice(SwordsList)

           if SwordName != "WoodenSword":
              SwordName = "Wooden Sword"

           InStock = [SwordName,SwordName1]

           DamageAmount = SwordsStats.get(SwordName).get("Damage")

           StaminaUsage = SwordsStats.get(SwordName).get("StaminaUsage")

           Price = SwordsStats.get(SwordName).get("Price")

           DamageAmount1 = SwordsStats.get(SwordName1).get("Damage")

           StaminaUsage1 = SwordsStats.get(SwordName1).get("StaminaUsage")

           Price1 = SwordsStats.get(SwordName1).get("Price")

           print(f"Swords In Stock: {InStock[0]}, {InStock[1]}")
           
           BuyInput = input("Pick Your Swords In Stock. ")

           if BuyInput == InStock[0]:
               print("You Are About To Buy: ",InStock[0])
               print(f"This Is The Stats, Damage: {DamageAmount} Stamina Usage:{StaminaUsage} Price: {Price} Coins")
               BuyInputCon = input("Do You Want To By This Sword? (Y/n) ")
               if BuyInputCon.lower() == "y":
                if P.Coins == Price:
                   InStock0 = True
                   SwordEquipped = True
                   EquippedSword = InStock[0]

                elif P.Coins < Price:
                   print("You Don't Have Enough Coins")

           elif BuyInput == InStock[1]:
                print("You Are About To Buy: ",InStock[1])
                print(f"This Is The Stats, Damage: {DamageAmount1} ,Stamina Usage: {StaminaUsage1}, Price: {Price1} Coins")
                BuyInputCon = input("Do You Want To By This Sword? (Y/n) ")
                if BuyInputCon.lower() == "y":
                 if P.Coins == Price:
                   InStock1 = True
                   SwordEquipped = True
                   EquippedSword = InStock[1]

                 elif P.Coins < Price:
                    print("You Don't Have Enough Coins")  
                   


                   

    elif TutorialInput.lower() == "t":
        TutorialInput = input("S To Increase Stamina ")
        if TutorialInput.lower() == "s":
            P.MaxStamina += 35
            print("Your Stamina Is: ",P.MaxStamina)
