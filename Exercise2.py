def Get_List(num1, num2): # return list from num1 to num2 excluding num2
    num1 = int(num1)
    num2 = int(num2)
    lst =[]
    change_rate = 1
    if num1 > num2:
        change_rate = -1
    current_num = num1
    while current_num != num2:
        lst.append(current_num)
        current_num += change_rate
    return lst

print(Get_List(-5, 2))