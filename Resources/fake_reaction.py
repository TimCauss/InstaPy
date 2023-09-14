import random
import time
from curses.ascii import isdigit


def fake_time_wait(proc, a=0.5, b=2):
    t = random.uniform(a, b)
    time.sleep(t)
    print(f'Process n°{proc} - Faking reaction time : {round(t, 3)}s')
