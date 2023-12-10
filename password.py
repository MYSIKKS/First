def ask_password(password):
    for i in range(3):
        input_password = input("введите пароль ")
        if password == input_password:
            print("Пароль принят")
            return
    print("В доступе отказано")


ask_password("password")
