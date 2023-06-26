#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    i = 0
    while (i < list_length):
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except IndexError:
            result_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        finally:
            i = i + 1
    return result_list
