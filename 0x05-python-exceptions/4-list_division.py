#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = 0
    my_list = []
    while i != list_length:
        try:
            result = my_list_1[i] / my_list_2[i]

        except IndexError:
            print("out of range")
            result = 0
            my_list.append(result)
            break
        except TypeError:  # different data type
            print("wrong type")
            result = 0
            my_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            my_list.append(result)
        except ValueError:
            result = 0
            my_list.append(result)
        finally:
            pass

        i += 1

    return my_list
