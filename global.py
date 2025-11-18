def hello():
    global name # i use a global name it not good but 
    name = 'jadi' # the first my name is mobin but with use globl i change name to jadi
    print(f'function name is {name}') # so i have one name first my name is mobin after that is a jadi


name = "mobin" # the first name is "mobin"
print(f'first name is {name}') # write mobin 
hello() # i call funtion
print(f'second name is {name}') # Because thsi line of code after function name is jadi