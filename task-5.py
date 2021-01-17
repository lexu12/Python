my_list = [7, 5, 3, 3, 2]
numb = int(input('введите число от 1 до 9'))
my_list.append(numb)
rating = sorted(my_list)
rating.reverse()
print(rating)