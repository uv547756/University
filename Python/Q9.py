
# Program to accept string as a password with stated requirements

up, low, flag = 0, 0, 0
passwd = input(str("Enter a password: "))
if len(passwd) >= 8:
    flag = 1
    for i in range(len(passwd)):
        if passwd[i].isupper():
            up += 1
        elif passwd[i].islower():
            low += 1
if (up >= 1 and low >= 1 and flag == 1):
    print("Password meets all requirements.")
else:
    print("All requirements don't meet")
    
