# -*- coding: utf-8 -*-
""""Console module Phone_directory
    
    A simple console module for working with the telephone directory
    Format  telephone directory - (Username, phone)
    See module copyreg for a mechanism for registering custom picklers.

    Functions:
        hello()
        phone_add(name, phone) --> add User Name, Phone
        phone_change(name, phone) --> change add User Name, NewPhone
        hello()


    Misc variables:

        __version__
        format_version
        compatible_formats
"""


class MoreArgument(Exception):
    pass


dict_users_phone = {"Oleksandr": '0950835767', "Yurii": '0994340909', }


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def input_error(func):
    # decorator
    def inner(*arg):
        try:
            result = func(*arg)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
        except TypeError:
            return 'Arguments is more'
        except MoreArgument:
            return 'Arguments is more'
    return inner


def hello():
    # outputs to the console on hello
    return f"How can I help you?"


@input_error
def phone_add(name, phone):
    # adds a new contact to the dictionary
    phone = sanitize_phone_number(phone)

    if name in dict_users_phone.keys():
        print(f'User {name} - exist with phone {dict_users_phone.get(name)}')
        if input("Replace (y - yes, n - no)").lower == 'y':
            dict_users_phone[name] = phone
            return f'User {name} update phone to {phone}'
        else:
            return f'User {name} - exist with phone {dict_users_phone.get(name)}'
    else:
        dict_users_phone[name] = phone
        return f'add to list {name}, {phone}'


@input_error
def phone_change(name, phone):
    # the new phone number of an existing contact
    phone = sanitize_phone_number(phone)
    dict_users_phone[name] = phone
    return f'for {name} change number to {phone}'


@input_error
def show_phone(name):
    # show("username") outputs the phone number for the specified contact to the console.
    if name in dict_users_phone.keys():
        return f'User {name} - have phone number {dict_users_phone.get(name)}'
    else:
        return f'and user {name} not exist'


def show_all():
    # outputs all phone number in list to the console.
    result = ''
    for key, value in dict_users_phone.items():
        result += f'(User, phone): {str(key)}, {value}\n'
    return result


def exit():
    print("Good bye!")
    return


dict_commands = {"hello": hello,
                 "add": phone_add,
                 "change": phone_change,
                 "phone": show_phone,
                 "show": show_all,
                 "exit": exit,
                 "goodbye": exit,
                 "close": exit
                 }


def action(func,  dictionary,  default="NO COMMAND"):
    if func in dictionary:
        return dictionary[func]
    return lambda * x:  default


def main():
    arg = ''
    print(f'main-code в {__name__} виконується тут')

    try:
        while True:
            command, *arg = input('>>>').strip().split(' ', 1)
            if arg:
                arg = arg[0].split(',')

            do = action(command, dict_commands)
            result = do(*arg)
            if not result:
                break
            print(result)

    except KeyboardInterrupt:
        print("Good bye!")


if __name__ == "__main__":
    main()
