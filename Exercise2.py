def Get_List(num1, num2): # return list from num1 to num2 excluding num2
    change_rate = 1
    if num1 > num2:
        change_rate = -1
    lst = list(range(num1, num2, change_rate))
    return lst

print(Get_List(9, 2))