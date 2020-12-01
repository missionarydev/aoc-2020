with open("day-01-input.txt", 'r') as f:
    numbers = []
    for line in f:
        numbers.append(int(line))

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(f"product: {numbers[i] * numbers[j]}, pair (i,j): {numbers[i]},{numbers[j]}")
                break
        else:
            continue
        break

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(
                        f"product: {(numbers[i] * numbers[j]) * numbers[k]}, triplet (i,j,k): {numbers[i]},{numbers[j]},{numbers[k]}")
                    break
            else:
                continue
            break
        else:
            continue
        break
