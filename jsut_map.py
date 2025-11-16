def tavan(x):
    return x ** 2


number = [2, 3, 4, 5, 6]

all_tavan = map(tavan, number)

print(list(all_tavan))