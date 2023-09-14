def split_words(words, num_temp):

    temp = [[] for _ in range(num_temp)]

    for i in range(len(words)):
        temp[i % num_temp].append(words[i])

    for i in range(num_temp):
        with open(f"temp{i + 1}.txt", "w") as f:
            f.write("\n".join(temp[i]))

    return temp


def password_list(path):
    with open(path, "r") as f:
        words = f.readlines()

    words = [word.strip() for word in words]
    return words


print(split_words(password_list('test.txt'), 6))
