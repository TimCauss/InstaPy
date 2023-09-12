import os
import random
import sys

import time
import logging

account = 'Tim0ut_13'
file_path = '../testcases/test.txt'
connexion_url = 'https://www.instagram.com/accounts/login/'

FORMAT = '%(asctime)s - %(levelname)s:%(message)s'
logging.basicConfig(filename='info-oop.log', filemode='w', encoding='utf-8', level=logging.INFO, format=FORMAT,
                    datefmt="%H:%M:%S")


def fake_time_wait():
    # This function simulates waiting for a random amount of time between 0.2 and 1.1 seconds.
    # Generate a random number between 0.2 and 1.1.
    t = random.uniform(0.2, 1.1)
    # Sleep for the random amount of time.
    time.sleep(t)
    # Log the amount of time that was waited.
    logging.info(f'Waiting random time between instructions: {t}')


def file_to_list(path):
    # This function takes a path to a file as input and returns a list of words
    with open(path, 'r') as f:
        # Read all the lines in the file.
        lines = f.readlines()
        # Split each line into a list of words.
        words = map(lambda line: line.split(), lines)
        # Return the list of words.
        return list(words)


base_dir = os.path.dirname(__file__) or '.'
sys.path.append("../..")

