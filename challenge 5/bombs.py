def answer(M, F):
    value = (int(M), int(F))
    generations = 0
    while True:
        bigger, smaller = value if value[0] > value[1] else (value[1], value[0])
        if smaller == 1:
            generations += bigger - smaller
            return str(generations)
        if smaller == 0:
            return 'impossible'
        generations += bigger // smaller
        value = (bigger % smaller, smaller) if value[0] > value[1] else (smaller, bigger % smaller)


print(answer('2', '4'))
