import random

System=random.randint(1,10)
user=int(input("Enter a number from 1 to 10 : "))

print(f"System number : {System}")
print(f"User number : {user}")

if System == user:
    print("Wow! You are Amazing.")
else:
    print("Sorry!, Please try again.")