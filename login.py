#code for login information with IF, ELIF & ELSE statement 27.06.2023

print("SECURE LOGIN")
username = input("Username? > ")
password = input("Password? > ")
if username == "mark" and password == "mak400":
  print()
  print("Welcome Mark!")
elif username == "kingsley" and password == "dokz" :
  print("Hi Mr Kingsley")
elif username == "Meike" and password == "mali":
  print("Hi Mama Mali!")
else:
  print("Login Failed, Go away!")