import math

try:
    imp = "import "+ input("Enter the module to be imported: ")
    exec(imp)
    n = {}
    n1, n2, k1, k2 = eval(input("Enter two numbers and their keys separated by comma (n1, n2, k1, k2): "))
    n[k1] = n1
    n[k2] = n2
    k1, k2 = eval(input("Enter the keys of numbers separated by comma: "))
    result = n[k1] / n[k2]
    m = int(input("Enter one more number: "))
    print("Result is:", result / math.sqrt(m))
    if (n[k1] == 0):
        raise RuntimeError
except ValueError:
    print("Invalid literal.")
except ImportError:
    print("Module not found.")
except ZeroDivisionError:
    print("Division by zero.")
except SyntaxError:
    print("Comma missing.")
except RuntimeError:
    print("May be meaningless.")
except KeyboardInterrupt:
    print()
    print("Program was interrupted.")
except KeyError:
    print("The requested key wasn't found.")
except:
    print("Something wrong in input.")
else:
    print("No exceptions.")
finally:
    print("Finally call is executed.")