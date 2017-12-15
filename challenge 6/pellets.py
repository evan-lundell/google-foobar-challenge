def answer(n):
    val = int(n)
    count = 0
    while val > 1:
        if val == 3:
            return count + 2
        if val % 2 != 0:
            if (val + 1) % 4 == 0:
                val = val + 1
            else:
                val = val - 1
            count += 1
        val = val / 2
        count += 1
    return count


print(answer(177))
