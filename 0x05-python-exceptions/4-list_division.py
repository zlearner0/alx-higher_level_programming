#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    my_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            my_list.append(result)
        except IndexError:
            print("out of range")
            result = 0
            my_list.append(result)
            continue
        except TypeError:  # different data type
            print("wrong type")
            result = 0
            my_list.append(result)
            continue
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            my_list.append(result)
            continue
        except ValueError:
            result = 0
            my_list.append(result)
            continue
        finally:
            pass

    return my_list
