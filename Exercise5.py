def is_Armstrong(num): # check if the number is belongs to armestrong numbers.
    if num < 100: # I added this condition here for using in other functions.
        return False
    ret_num = 0
    for x in str(num):
        ret_num += int(x) ** len(str(num)) # sum of all power numbers in num
    if ret_num == num:
        return True
    return False

def get_armstrong_list(num): # get a list that contains armestrong numbers.
    Armstrong_lst = []
    if num < 100: # I added this condition here as well so that there is no overload in the program.
        return Armstrong_lst
    for number in range(num):
        if is_Armstrong(number):
            Armstrong_lst.append(number)
    return Armstrong_lst

try:
    num = int(input("Enter a number : "))
    print(get_armstrong_list(num))
except ValueError:
    print("That is not a number!")