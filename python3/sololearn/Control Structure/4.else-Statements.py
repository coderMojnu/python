user = input("Enter your user name: ")
if user == "Mojnu" or "Mominul" or "Mehedy":
 password = input("Enter your Password please: ")
 if password == "abc":
  print("You are Succesfully log in")
 else:
  print("sorry")
else:
 print("You forget username. Do you want to recover your username?")
 answer = input()
 if answer == "yes":
  forget = input("Your age: ")
  if forget == "22":
   print("your user name is Mojnu")
  else:
   print("Sorry")