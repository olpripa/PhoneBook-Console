
def add_contact(name, phone):
    return f"User {name} added contact {phone}"


def show_phone(name):
    return "User {name} showing phone"


def show():
    return "Show all data"


def unknown_command(command):
    return f"Not command {command}"


commands = {'add': add_contact, 'show': show_phone, 'all': show}


def main_example():
    command, *data = input().strip().split(' ', 1)
    if commands.get(command):
        handler = commands.get(command)
        if data:
            data = data[0].split(',')
        # та зараз саме цікаве починається
        # handler може бути функцію або add_contact або show_phone або show
        # і кожна функція очікує різну кількість аргументів,
        # но ми знаємо що кільсть отриманих від користувача данних
        # має дорівнювати кількості очікуванних аргументів самої функції
        # тому ми можемо зробити так
        result = handler(*data)
        # детальніше
        # коли ми викликаємо функцію у такій спосіб - значення аргументів буде отримане із значеннь переданого списку
        # це теж саме що name, phone = ["Jon Born", "345 668 900"]
        # вот послідовність у спрощеному виді процессу виклику функції
        # add_contact(*data) => add_contact(*["Jon Born", "345 668 900"]) => add_contact("Jon Born", "345 668 900" )
        # і якщо data = [] (тобто немає додаткових даних) і ми викликаємо handler який зараз є show
        # show(*data) => show(*[]) => show()

    else:
        # тут якщо не має команди ми просто викличемо unknown_command
        result = unknown_command(command)

    print(result)
