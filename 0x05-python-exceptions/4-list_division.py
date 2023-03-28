#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    new_list = []
    while n < list_length:
        try:
            result = my_list_1[n]/my_list_2[n]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
            n += 1
    return new_list

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)    
