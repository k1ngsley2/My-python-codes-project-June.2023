#this code was done on 20.june.2023
#add \033[31m before a print line and \033[0m to make yor print red color 
#note that number 33 is for black color 
#for more color code see this list below
#Default	0, #Black	30, #Red	31, #Green	32, #Yellow	33 #Blue	34, Purple	35, Cyan	36, White	37
print ("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")

yourName = input("What is your name? ")
EnemyName = input("What is your worst enemy’s name? ")
SuperPower = input("What is your superpower? ")
Live = input("Where do you live? ")
Food = input("What is your favorite food? ")

print ("Hello", yourName, "Your ability to", SuperPower, "will make sure you never have to look at", EnemyName, "again. Go eat your", Food, "as you walk down the streets of", Live, "and use" , SuperPower, "for good and not evil!")