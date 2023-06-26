#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    i = 0
    while (i < list_length):
        try:
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except IndexError:
            result_list.append(0)
            print("out of range")
        except ZeroDivisionError as e:
            result_list.append(0)
            print(e)
        finally:
            i = i + 1
    return result_list
