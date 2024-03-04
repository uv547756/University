
#Program to find if entered string is palindrome or not

string1 = input(str("Enter a String: "))
flag = 0
for i in range(len(string1)):
    for j in range(len(string1)-1,-1,-1):
        if string1[i] == string1[j]:
            flag = 1
if flag==1:
    print(string1,"is palindrome")
