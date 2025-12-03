import random, time

comp_turn = ('k', 'n', 'b')


def knb_choice(t):
    if t == 'k':
        print('камень')
    elif t == 'n':
        print('ножницы')
    elif t == 'b':
        print('бумага')


running = True


def main():
    global running

    while running:
        turn = input('Сделайте свой ход : k = камень, n = ножницы,  b =  бумага, e = выход    :')

        time.sleep(0.5)

        if turn == 'e':
            print(' Выход ')
            time.sleep(5)
            running = False
        elif turn not in ('e', 'k', 'n', 'b'):
            print(' Ошибка ввода, начните пожалуйста снова')
            continue

        else:
            knb_choice(turn)
            c_turn = random.choice(comp_turn)
            knb_choice(c_turn)
            if (turn == 'k' and c_turn == 'n') or (turn == 'n' and c_turn == 'b') or (turn == 'b' and c_turn == 'k'):
                print('Вы выиграли!')

            # count [0] == ++1
            if (turn == 'n' and c_turn == 'k') or (turn == 'b' and c_turn == 'n') or (turn == 'k' and c_turn == 'b'):
                print('Я выиграл!')


if __name__ == '__main__':
    main()