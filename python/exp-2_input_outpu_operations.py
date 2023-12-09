n = float(input("Enter the nummber (n): "))
print("Square root of n is:", n ** (0.5))

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area =", l * b, "\nPerimeter =", l + b)

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = a
a = b
b = c
print("After swapping:")
print("a =", a, "\nb =", b)

List = ['meet', '20', 'hi']
Set = {'meet', '20', 'hi'}
Tuple = ('meet', '20', 'hi')
print(f'Before\nList={List}\nSet={Set}\nTuple={Tuple}\n')
Add = input('enter to append: ')
List.append(Add)
Set.add(Add)
Tuple_L = list(Tuple)
Tuple_L.append(Add)
Tuple = tuple(Tuple_L)
print(f'Before\nList={List}\nSet={Set}\nTuple={Tuple}\n')

print('for loop implementation')
h = int(input("Enter height of pyramid: "))
for i in range(1, h + 1):
    for j in range(i):
        print(i, end = " ")
    print()

print('while loop implementation')
n = int(input("Enter the number: "))
tmp = n
result = 1
while n >= 1:
    result *= n
    n -= 1
    if tmp == 0:
        result = 1
print('Factorial(n) =', result)

print('if ... else implementation')
n = int(input("Enter the number: "))
if n % 2 == 0:
    print("Number is even.")
else:
    print('Number is odd.')