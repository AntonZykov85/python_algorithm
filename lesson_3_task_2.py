import hashlib, uuid

def get_hash():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hashed_object = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    return login, hashed_object


def registration():
    print('регистрация пользователя')
    login, reg_hash = get_hash()
    with open('users_db.txt', 'r') as f:
        open_file = f.read()
        if reg_hash in open_file:
            print("Вы уже зарегистрированы в системе, выполните вход.")
        else:
            with open('users_db.txt', 'a+') as f:
                f.write(reg_hash + '\n')
                print('Регистрация прошла успешно')

def log_in():
    print('вход в систему')
    login, check_hash = get_hash()
    with open('users_db.txt', 'r') as f:
        open_file = f.read()
        if check_hash in open_file:
            print("Добро пожаловать!")
        else:
            print('вы ввели неверные данные или не зарегистрированы в системе!')
            return registration()



log_in()
