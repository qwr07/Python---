user_name =input("Enter your name:")

while True :
  try: 
     num = int(input(f"{user_name},Enter your number:"))
     if num %2==0 and num> 10:
       print(f"{user_name}, the number is even and big")
     elif num %2==0 and num< 10:
       print(f"{user_name}, the number is even and small")
     elif num %2 !=0 and num> 10:
       print(f"{user_name}, the number is odd and big")
     else:
        print(f"{user_name}, the number is odd and small")
  except ValueError: 
       print(f"{user_name}, please enter a valid number!")
       continue
  again = input(f"{user_name}, do you want to try another number? (yes/no): ").strip().lower()
  if again !="yes":
       print(f"Thanks for using the program, {user_name}! 👋")
       break
