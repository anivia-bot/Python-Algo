def power(num, mm, count):
    if num < 1:
        print((mm*0.91)/1000)

        return
    print(f'M&M Day {count} :', mm)
    count += 1
    mm *= 2
    return power(num - 1, mm, count)

power(365, 1, 1)
a = 4503599627370496
b = 2199023255552

print(a/b)