#regular functions
def perfect(num):
    Sum = 0
    for i in range(1, num):
        if num % i == 0:
            Sum=Sum+i
        return Sum == num

n = int(input("Enter a number: "))
res = perfect(n)
print(res, ".", sep="")
if res == False:
    print("Entered number is not a perfect number.")
else:
    print("Entered number is a perfect number.")

#lambda function
a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
maximum = lambda a, b: a if a > b else b
print(f"Maximum of {a} and {b} is {maximum(a, b)}.")