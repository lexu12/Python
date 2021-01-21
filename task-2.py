def ques_func(name, sername, year_birth, town, email, tel):
    return f' name - {name}, sername-{sername}, year_birth-{year_birth},town-{town}, email-{email}, tel-{tel}'


print(ques_func(name=input('Введите имя'), sername=input("Введите фамилию"), year_birth=input("Введите год рождения"),
                town=input("Введите город прроживания"),
                email=input("Введите адрес электронной почты"), tel=input("Введите номер телефона")))
