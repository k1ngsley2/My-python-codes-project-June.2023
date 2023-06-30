#This code is for IF and Else statements with color fonts. 23.06.2023
Myname = input("what is your name?: ")
if Myname == "kingsley":
  print("\033[32mWelcome King!\033[0m")
  print("\033[32mYou are a rockstar!!!\033[0m")
else:
  print("\033[31mWho the hell are you?\033[0m")
  print("\033[33mAccess denied!\033[0m")
YourPet = input("Do you prefer cats or dogs?: ")
if YourPet == "cats":
  print("\033[32Meow!!!\033[0m")
else:
  print("\033[33mWoof!!!!!!\033[0m")