from math import ceil


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'[CONSUMER] Consuming {n}...')
        r = '200 OK'


def produce(c):
    c.send(None)
    for n in range(1, 6):
        print(f'[PRODUCER] Producing {n}...')
        r = c.send(n)
        print(f'[PRODUCER] Consumer return: {r}')
    c.close()


c = consumer()
produce(c)
