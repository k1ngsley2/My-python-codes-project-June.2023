#This code is a basic weight converter 30.06.2023 add int for whole number inputs or float for decimal number inputs 
print()
print("Welcome to Kingsley's Weight Converter")
print()
YourWeight = int(input(" what is your weight?: "))
Unit = input("Is your weight in (K)g or (L)bs?; ")
if Unit == "k" or Unit == "K":
  convert = YourWeight / 0.45
  print("Your Weight in Kilogram: " + str(convert)) #you have to add the str in order value to be displayed
  print()
elif Unit == "L" or Unit == "l":
  convert2 = YourWeight * 0.45
  print("Your Weight in Pounds: " + str(convert2))
  print()
else:
  print("Invalid unit or Weight, Please check the data given!!")