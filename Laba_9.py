import random
from loguru import logger

logger.remove(handler_id=None)
logger.add('laba_9.log', format='{time} {level} {message}', level='INFO', rotation='10 KB', compression='zip')

while True:
    try:
        n = int(input('Введите число '))
        k = int(input('Введите число попыток '))
        logger.info(f'Введено число {n}')
        logger.info(f'Введено число {k}')
        break
    except ValueError:
        print("Вводите число ")
        logger.error("ValueError", exc_info=True)

p = list(range(1, n + 1))
t = random.choice(p)
logger.info(f'Компьютер загадал число  {t}')

v = 1
while True:
    while True:
        try:
            x = int(input('как вы думаете, какое число загадал компьютер :'))
            logger.info(f'попытка {v} Введено {x}')
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
            logger.info(f'Число {t} угадано')
            break
    else:
        print(' Неверно \nПопытки закончились')
        logger.info(f'попытки закончились')
        break
    v += 1
