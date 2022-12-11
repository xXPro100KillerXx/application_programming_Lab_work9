import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        n = int(input('Введите число '))
        k = int(input('Введите число попыток k)'))
        logging.info(f'Введено число {n}')
        logging.info(f'Введено число {k}')
        break
    except ValueError:
        print("Вводите число ")
        logging.error("ValueError", exc_info=True)

p = list(range(1, n + 1))
t = random.choice(p)
logging.info(f'Компьютер загадал число  {t}')

v = 1
while True:
    while True:
        try:
            x = int(input('как вы думаете, какое число загадал компьютер :'))
            logging.info(f'попытка {v} Введено {x}')
            break
        except ValueError:
            print(" Вводите число ")
    if v < k:
        if x < t:
            print('ваше число меньше t')
        elif x > t:
            print('ваше число больше t')
        elif x == t:
            print('Вы угадали')
            logging.info(f'Число {t} угадано')
            break
    else:
        print(' Неверно \nПопытки закончились')
        logging.info(f'попытки закончились')
        break
    v += 1