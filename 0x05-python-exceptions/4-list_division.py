def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if type(my_list_1[i]) == int or         type(my_list_1[i]) == float:
                if type(my_list_2[i]) == int or type(my_list_2[i]) == float:
                    result = my_list_1[i] / my_list_2[i]
                else:
                    print("wrong type")
            else:
                print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
