n = int(input("Enter the count of numbers: "))
print("Enter", n, "numbers:")
with open("T1.txt", "w") as f:
    for i in range(n - 1):
        f.write(str(input()) + "\n")
    f.write(str(input()))

with open("T1.txt", "r") as f1, open("T2.txt", "w") as f2:
    l = list()
    for line in f1:
        l.append(int(line))
    l.sort()
    for i in range(n - 1):
        f2.write(str(l[i]) + "\n")
    f2.write(str(l[n - 1]))