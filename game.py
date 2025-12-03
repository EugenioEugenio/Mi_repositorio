import random , time

user_score = 0
computer_score = 0

comp_turn = ('k','n','b')

def knb_choice(t):
    if t=='k':
        print('камень')
    elif t=='n':
        print('ножницы')
    elif t=='b':
        print('бумага')

running = True

def main():
    global running
    global user_score
    global computer_score

    while running:
        turn = input('Сделайте свой ход : k = камень, n = ножницы,  b =  бумага, e = выход    :')

        time.sleep (0.5)

        if turn == 'e':
            print(' Выход ')
            time.sleep  (5)
            running=False
        elif turn not in ('e' ,'k' , 'n' , 'b'):
            print(' Ошибка ввода, начните пожалуйста снова')
            continue

        else:
            knb_choice(turn)
            c_turn = random.choice(comp_turn)
            knb_choice(c_turn)
            if (turn == 'k' and c_turn == 'n') or (turn == 'n' and c_turn == 'b') or (turn == 'b' and c_turn == 'k'):
                user_score += 1
                print('Вы выиграли!')

            if (turn == 'n' and c_turn == 'k') or (turn == 'b' and c_turn == 'n') or (turn == 'k' and c_turn == 'b'):
                print('Я выиграл!')
                computer_score +=1

            print(f"Счёт - Вы   {user_score}  :  {computer_score}  Машина" )
        if user_score==10 or computer_score== 10:
            print('Хватит ерундой заниматься, идите учить PYTHON!' )
            time.sleep  (10)
            running=False


if __name__ == '__main__':
    main()
