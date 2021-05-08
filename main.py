"""
Universidad de Carabobo
FaCyT - Ciencias de la Computación
Electiva - Recuperación de Información
Prof. Giugni, Marylin
Mayo - 2021
Br. GIL, Franco - fgil1@uc.edu.ve

Ref: https://ccc.inaoep.mx/~mmontesg/pmwiki.php/Main/RecuperacionDeInformacion

TODO: Add argparse
TODO: Agg logs to see the output
TODO: Implement with threads and improve the speedp.
"""
import time

from util.homework import Homework


if __name__ == '__main__':
    past = int(time.time())

    Homework.homeWork1()
    # Homework.homeWork2()

    now = int(time.time())

    print(f'Homework #1 - End. Time elapsed: {now - past} second(s)')
