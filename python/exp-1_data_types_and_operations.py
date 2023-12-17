# data types
print('Numeric:')
integer = 1
floating = 1.11
x = 5
y = 3
z = complex(x,y)

print('Integer', integer)
print(type(integer))
print ("The real part of complex number is : ",z.real)
print (type(z.real))
print ("The imaginary part of complex number is : ",z.imag)
print (type(z.imag))
print('Float', floating)
print(type(floating), '\n')

print('Dictionary:')
Dictionary = {
    'name': 'Meet Patel'
}
print(Dictionary)
print(type(Dictionary), '\n')

print('Boolean:')
print(True)
print(type(True), '\n')

print('List:')
List = ['Hi', '20', 'how', 'u', 'doinnn', 20]
print(List)
print(type(List), '\n')

print('Set:')
Set = {'Meet', 'hi', 20, 20, 20}
print(Set)
print(type(Set), '\n')

print('Tuple:')
Tuple = ('Meet', 'hi', 20, 20)
print(Tuple)
print(type(Tuple), '\n')

print('String:')
String = 'this is a string'
print(String)
print(type(String), '\n')

#operations
x = 20
y = 5
print(f'x={x}, y={y}')
print('Arithmetic:')
print(f'x+y={x+y}')
print(f'x-y={x-y}')
print(f'x*y={x*y}')
print(f'x/y={x/y}')
print(f'x%y={x%y}\n')

print('Comparison:')
print(f'x>y={x>y}')
print(f'x<y={x<y}')
print(f'x==y={x==y}')
print(f'x!=y={x!=y}')
print(f'x>=y={x>=y}')
print(f'x<=y={x<=y}\n')

print('Logical:')
print(f'x AND y={x and y}')
print(f'x OR y={x or y}')
print(f'NOT y={not y}\n')

print('Assignment:')
print(f"x += y: {x + y}")
print(f"x -= y: {x - y}")
print(f"x *= y: {x * y}")
print(f"x /= y: {x / y}")
print(f"x %= y: {x % y}\n")

print('Bitwise:')
print(f'x&y: {x&y}')
print(f'x|y: {x|y}')
print(f'~y: {~y}')
print(f'x^y: {x^y}')
print(f'x>>y: {x>>y}')
print(f'x<<y: {x<<y}')