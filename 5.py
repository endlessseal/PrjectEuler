def solve():
    counter = 20
    numbers_to_check = list(range(1,21))
    while True:
        for each in numbers_to_check:
            if counter % each != 0:
                break
        else:
            print(counter)
            return True
        counter += 1

solve()
