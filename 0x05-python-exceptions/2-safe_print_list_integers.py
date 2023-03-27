#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = []
    if x == 0:
        try:
            print("{:d}".format(my_list[0]), end="")
        except ValueError:
            pass
        else:
            new_list.append(my_list[0])
    else:
        for item in range(0, x):
            try:
                print("{:d}".format(my_list[item]), end="")
            except ValueError:
                continue
            except TypeError:
                continue
            except IndexError:
                break
            else:
                new_list.append(my_list[item])
    print("")
    summ = 0
    for item in new_list:
        summ += 1
    return summ
