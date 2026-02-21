name=(input("enter your name:")).strip().lower()
with open("data.txt","r") as file:
 data=  data = [user.strip().lower() for user in file]
if name in data :
   print("good")
else:
   print("not good ")
   choice =input("Do you want to register? (yes/no):").lower()
   if choice =="yes":
       with open("data.txt", "a") as file:
         file.write(name+"\n")
   elif choice =="no" :
      print("goodbye")
