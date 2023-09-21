import random
from datetime import datetime

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', "'", '(', ')',
        '*', '+', '-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


number_words = 100

def word_creator(password=''):
    for _ in range(round(random.uniform(6, 15))):
        password += str((random.choice(char)))
    return password


def words_generator(nbr=10):
    for i in range(nbr):
        file.write(word_creator() + '\n')


if __name__ == '__main__':
    file = open('test.txt', 'a')
    time1 = datetime.now()
    words_generator(number_words)
    speed = (datetime.now() - time1)
    print(f'[{number_words}] words generated in: {speed.total_seconds()} seconds')
    file.close()
