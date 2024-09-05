def age_check(age):
    try:
        int(age)
    except ValueError:
        return False
    return True if int(age) >= 18 else False


def citizen_check(citizen):
    return True if citizen.lower() in ['россия', 'российская федерация'] else False


def criminal_check(criminal):
    return True if criminal.lower() in ['нет', 'no'] else False


def error_print():
    print('Вам не доступно голосование!!')
    exit()


def main_opros():
    print('Вас приветствует программа выдачи жетонов голосования!\nДля получения жетона отвечайте на вопросы,'
          'строго следуя инструкции к каждому вопросу\n')
    if not age_check(input('Укажите возраст (только цифры): ')):
        return error_print()
    if not citizen_check(input('Укажите страну гражданства (по-русски): ')):
        return error_print()
    if not criminal_check(input('Есть ли у вас судимость (да/нет):')):
        return error_print()
    return print('Для получения жетона, пройдите к окну № 4')


if __name__ == '__main__':
    main_opros()
