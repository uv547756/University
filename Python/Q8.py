
''' Program to print given string(s) [Q8]

string1 = input(str("Enter a string: ")); print(string1)
for i in range(len(string1)):
               string2 = string1[-1]+string1[:-1]
               print(string2)
               string1
               print()
'''
string1 = "SHIFT"
for i in range(len(string1)+1):
    lis2=string1[i:]+string1[:i]
    print(lis2)
    


