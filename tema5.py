while True:
    try:
        user_input = input('Как работает встроенная функция reversed(): ')
        if user_input.startswith('reversed') and len(user_input) > len('reversed'):
            print(tuple(eval(user_input)))
            break

        else:
            print("Где-то Вы ошиблись, попробуйте ещё раз...")
            continue

    except SyntaxError:
        print("Где-то Вы ошиблись, попробуйте ещё раз please...")