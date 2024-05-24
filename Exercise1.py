          # Exercise 1.1
def Get_Sum(lst): # get the sum of all item in the list
    totaal = 0
    for item in lst:
        totaal += item
    return totaal

   # Exercise 1.2
def Get_Sum_NonDuplicates(lst): # get the sum of all item in the list
    totaal = 0
    st = set(lst)
    for item in st:
        totaal += item
    return totaal

   # Exercise 1.3
my_lst = [1, 2, 3, 4, 4, 3, 2, 1]
print(f" the sum of all of the numbers in list = {Get_Sum(my_lst)}")
print(f" the sum of all of the numbers in list ' excluding the duplicates' = {Get_Sum_NonDuplicates(my_lst)}")