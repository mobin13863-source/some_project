def tavan(x):
    return x ** 2



number = [2, 4 ,65, 7]


for i in range(len(number)):
    (number[i]) = tavan(number[i])
    
          
print(number)   # this way a amator or public and that is a simple


print('\n')


number_2 = [2, 4 ,65, 7]


def tavan_2(j):
    return j ** 2


all_tavan = map(tavan_2, number_2)


print(list(all_tavan))
# or i can write this 


print()

all_tavan_2 = map(tavan_2, number_2)
for i in all_tavan:
    print(i)

