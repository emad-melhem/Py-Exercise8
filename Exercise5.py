def get_Armstrong(num):
    Armstrong_lst = []
    for number in range(num):
        if number < 100:
            continue
        ret_num = 0
        for x in str(number):
            ret_num += int(x) ** len(str(number))
        if ret_num == number:
            Armstrong_lst.append(number)
    return Armstrong_lst

num = int(input("Enter a number : "))
print(get_Armstrong(num))