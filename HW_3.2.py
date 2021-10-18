#Реализовать функцию, принимающую несколько параметров,
#описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать
#параметры как именованные аргументы. Реализовать вывод данных
#о пользователе одной строкой.



def user_name (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(user_name(surname = 'Иванов', name = 'Иван', year = '1980', city = 'Иваново', email = 'ivan1980@mail.ru', telephone = '8-999-999-99-99'))
