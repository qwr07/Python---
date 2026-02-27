
user ={
        "shahad":89463,
        "ddjj":3973
    }
user = input("Enter your username:")
password =int(input("Enter your password:"))
if user in tt and tt[user] == password:
        print("yes")
        score =0
        while True:
           print("1- Add Score")
           print("2- Show Score")
           print("3- Exit")
           choice = input("Choose: ")  
           if choice == "1":
               try:
                   score += int(input("Enter score to add: "))
               except ValueError:
                   print("Invalid input. Please enter a number.")
           elif choice == "2":
               print("Current score:", score)
           elif choice == "3":
               print("Exiting the program. Goodbye!")
               break 
