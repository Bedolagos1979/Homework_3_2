a = input(print('сколько вам лет?'))
b = input(print('как вас звать?'))
while a == a:
    if a.isdigit():
        a = int(a)

        if a > 1 and a < 9:
            print('приет, шкет ' + b)
            a = str(a)
            a = input(print('сколько вам лет?'))
            b = input(print('как вас звать?'))
        elif a >= 10 and a <= 18:
            print(' привет, как жизнь? ' + b)
            a = str(a)
            a = input(print('сколько вам лет?'))
            b = input(print('как вас звать?'))
        elif a > 18 and a < 100:
            print('здравстуйте ' + b + ', что желаете???')
            a = str(a)
            a = input(print('сколько вам лет?'))
            b = input(print('как вас звать?'))
        elif a > 100 and a < 100000000:
            print('ты че даун ' + b + '. Думай головой что следующий раз писать!!!')
            a = str(a)
            a = input(print('сколько вам лет?'))
            b = input(print('как вас звать?'))
        elif a <= 0:
            print('дурачек ' + b + '? Пробуй еще!')
            a = str(a)
            a = input(print('сколько вам лет?'))
            b = input(print('как вас звать?'))
