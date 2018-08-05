total = 2
first = 1
second = 2

while True:

    added = first + second
    if added > 4000000:
        break
    if added % 2 == 0:
        total += added
    first = second
    second = added

    print(added, total

print(total
