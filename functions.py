"""program Caesar"""


""" 
encryption_caesar - функция шифрования(переименовал с encryptionСaesar потому, что название функции по пеп 8 должно
быть в нижнем регистре о чем и сигнализировал Pycharm  подчеркивая название.)
Реализована по простой логике: функция 'ord' переводит в цифру, соответствующую знаку в таблице Unicode, прибавляю 
шаг "shift" далее с помощью функции 'chr' возвращаем символом Unicode соответствующий
полученному числовому значению.

decryption_caesar - - функция шифрования(переименовал по аналогичной логике как и с encryption_caesar)
Реализована также по простой логике: 'ord' переводит в цифру, соответствующую знаку в таблице Unicode, отнимаю 
шаг "shift" далее с помощью функции 'chr' возвращаем символом Unicode соответствующий 
полученному числовому значению.
"""


def encryption_caesar(text: str, shift: int) -> str:
    x: str = ''
    for letter in text:
        x += chr(ord(letter)+shift)
    return x


def decryption_caesar(text: str, shift: int) -> str:
    x: str = ''
    for letter in text:
        x += chr(ord(letter)-shift)
    return x


if __name__ == '__main__':
    try:
        message = input("'Шифровать' или 'Расшифровать'? ").lower()
        if message == "шифровать":
            sms: str = input("Введите строку которую необходимо зашифровать ")
            shifter: int = int(input("Укажите шаг смещения в цифрах "))
            print(f"Зашифрованное сообщение - '{encryption_caesar(sms, shifter)}'")
        elif message == "расшифровать":
            sms: str = input("Введи то, что необходимо расшифровать ")
            shifter: int = int(input("Укажите шаг смещения в цифрах "))
            print(f"Расшифрованное сообщение -  '{decryption_caesar(sms, shifter)}'")
        else:
            print("Шифровать и дешифровать можно только строку, шаг смещения принимает в себя только цифры ")
    except ValueError:
        print("Необходимо ввести численное значение ")
    except KeyboardInterrupt:
        print("\nПрограмма прервана.\n При необходимости запустите ее заново. ")
    finally:
        print("Программа завершила работу. ")
