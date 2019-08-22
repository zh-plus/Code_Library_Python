import random
import string


def random_string(string_len=10000):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(string_len))


def random_tuple(n=10000):
    r = range(n)
    return ' '.join([str(random.choice(r)), str(random.choice(r))])


def generate():
    result = []
    n = 10000
    result.append(str(n))
    for _ in range(n):
        result.append(random_string())

    for _ in range(1):
        result.append(random_tuple(n))

    return '\n'.join(result)


if __name__ == '__main__':
    with open('in.txt', 'w') as f:
        f.write(generate())
