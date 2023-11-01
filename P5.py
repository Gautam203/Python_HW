# Python program to swap two numbers using bitwise operator

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

x=x^y
y=x^y
x=x^y

print('The value of x after swapping: ' ,x)
print('The value of y after swapping: ', y)
