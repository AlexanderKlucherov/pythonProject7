"""program Caesar"""


""" 
encryption_caesar - функция шифрования(переименовал с encryptionСaesar потому, что название функции по пеп 8 должно
быть в нижнем регистре о чем и сигнализировал Pycharm  подчеркивая название.)
Реализована по простой логике: функция 'ord' переводит в цифру соответствующую знаку в таблице Unicode прибавляю 
шаг "shift" и все это с помощью функции 'chr' возвращаем символом Unicode соответствующий
полученному числовому значению.

decryption_caesar - - функция шифрования(переименовал по аналогичной логике как и с encryption_caesar)
Реализована также по простой логике: 'ord' переводит в цифру соответствующую знаку в таблице Unicode отнимаю 
шаг "shift" и все это с помощью функции 'chr' возвращаем символом Unicode соответствующий 
полученному числовому значению.
"""


def encryption_caesar(text: str, shift: int) -> str:
    x = ''
    for i in range(len(text)):
        x += chr(ord(text[i])+shift)
    return x


def decryption_caesar(text: str, shift: int) -> str:
    x = ''
    for i in range(len(text)):
        x += chr(ord(text[i])-shift)
    return x


if __name__ == '__main__':
    try:
        message = input("'Шифровать' или 'Расшифровать'? ").lower()
        if message == "шифровать":
            sms = input("Введите строку которую необходимо зашифровать ")
            shifter = int(input("Укажите шаг смещения в цифрах "))
            print("Зашифрованное сообщение - ", "'" + encryption_caesar(sms, shifter) + "'")
        elif message == "расшифровать":
            sms = input("Введи то, что необходимо расшифровать ")
            shifter = int(input("Укажите шаг смещения в цифрах "))
            print("Расшифрованное сообщение - ", "'" + decryption_caesar(sms, shifter) + "'")
        else:
            print("Шифровать и дешифровать можно только строку, шаг смещения принимает в себя только цифры ")
    except ValueError:
        print("Необходимо ввести численное значение ")
    except KeyboardInterrupt:
        print("\nПрограмма прервана.\n При необходимости запустите ее заново. ")
    finally:
        print("Программа завершила работу. ")
