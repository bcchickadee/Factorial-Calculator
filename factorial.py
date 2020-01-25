def programsequence(x):
    if int(x)==0:
        print('1')
    elif int(x)==1:
        print('1')
    elif int(x)>1:
        print(factorial(x))
    else:
        print('Error: You should input an integer which is not smaller than 0')

def factorial(x):
    if x==1:
        return 1
    else:
        return factorial(int(x)-1) *int(x)
        
print('Factorial Calculator')
print('Developed by bcchickadee')
print('ver 3.5 Jan 25 2020')
while 0==0:
    num=input('Enter an integer.\n')
    print('The answer is:')
    programsequence(num)
    print('\n')
