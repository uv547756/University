

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

user_input = input("Enter elements of the list seperated by spaces: ")
user_list = user_input.split()
reversed_list = reverse_list(user_list)
print("Reversed list: ", reversed_list)

