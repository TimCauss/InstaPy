c = 0

def add_count(ct):
    global c
    c += ct

def count():
    return c

def count_to_percent(words):
    return round(100 * c // words)
