print("=== PASSWORD VALIDATOR ===")
while True: 
  password = input("\nEnter a password: ")

  upper = False
  lower = False
  number = False
for char in password:
    if char >="A" and char <="Z":
        upper = True
    if char >= "a" and char <="z":
        lower = True
    if char >="0" and char <=9:
        number = True
valid = True
if len(password)<8: 
    print("password must have at least 8 characters")
    valid = False
if upper == False:
    print("Pasword must contain an uppercase letter")
    valid = False
if lower == False:
    print("password must contain a lowercase letter")
    valid = False
if number = False:
    print("pasword must contain a number")
    valid = False
if valid == True:
  print("\Password is valid!")
else:
  print("nInvalid password. Try again")
