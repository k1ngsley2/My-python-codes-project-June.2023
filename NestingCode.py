#This is a nesting code for several IF and ELIF statements. 27.06.2023

Tvshow = input("What is your favorite tv show? ")
if Tvshow == "Manifest":
  print("Really, coool!")
  favoriteCharacter = input("who is your favorite character? ")
  if favoriteCharacter == "Carl":
    print()
    print("Yeah, he was the dragon!")
  if favoriteCharacter == "Michealla":
    print()
    print("Yeah!! she was also amazing gem")
  else:
    print("You don't know the best character atall")
elif Tvshow == "Empire":
  print()
  print("That was also amazing show but not the favorite i expected from you")
elif Tvshow == "Mad Dogs":
  print()
  print("You got to be kiding me right?")
  kidding = input("Are you kidding right now? ")
  if kidding == "yes":
    print("You need to get a coffee")
  elif kidding == "no":
    print("You should go get cold water!")
else:
  print("You should watch \033[35mManifest\033[0m Tv Serie and you will change your opinion!")