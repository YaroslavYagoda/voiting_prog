"""
Задание:
Напишите программу, которая проверяет, можно ли человеку голосовать на выборах.
Условия:
Возраст должен быть 18 лет или старше.
Человек должен быть гражданином страны.
Человек не должен быть дисквалифицирован (например, по причине уголовного наказания).
"""


def age_check(age):
    try:
        int(age)
    except Exception:
        return False
    return True if int(age) >= 18 else False


def citizen_check(citizen):
    country1 = 'россия'
    country2 = 'российская федерация'
    return True if citizen.lower() == country1 or citizen.lower() == country2 else False


def criminal_check(criminal):
    return True if criminal.lower() == 'нет' or criminal.lower() == 'no' else False


print('Вас приветствует программа выдачи жетонов голосования!\nДля получения жетона отвечайте на вопросы,'
      'строго следуя инструкции к каждому вопросу\n')
if not age_check(input('Укажите возраст (только цифры): ')):
    print('Вам не доступно голосование!!')
    exit()
if not citizen_check(input('Укажите страну гражданства (по-русски): ')):
    print('Вам не доступно голосование!!')
    exit()
if not criminal_check(input('Есть ли у вас судимость (да/нет):')):
    print('Вам не доступно голосование!!')
    exit()
print('Для получения жетона, пройдите к окну № 3')
