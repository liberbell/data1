def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        ret = 'fizzbuzz'
    elif num % 3 == 0:
        ret = 'fizz'
    elif num % 5 == 0:
        ret = 'buzz'
    else:
        ret = str(num)
    return ret

for num in range(1,101):
    print(fizzbuzz(num))
