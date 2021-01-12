time = int(input('Введите время в секундах'))
seconds = time % 60
minutes = ((time % 3600)//60)
hours = time//3600
print(f' чч:{hours} мм:{minutes} сс:{seconds}')