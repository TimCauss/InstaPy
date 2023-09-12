import random
import time


def fake_time_wait(proc):
    t = random.uniform(0.5, 2)
    time.sleep(t)
    print(f'Process n°{proc} - Faking reaction time : {round(t, 3)}s')
