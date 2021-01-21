def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    new_my_list = sorted(my_list)
    new_my_list.pop(0)
    return sum(new_my_list)


print(my_func(10, 7, 8))