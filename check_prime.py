number = int(input ('Enter any numbers: '))
count = 0
for i in range(1,number):
    if number%i==0:
        count +=2
    else:
        pass

if count ==2:
    print(number,'is prime number')
else:
    print(number,'is not a prime number')