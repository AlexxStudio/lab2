def int_check(a):
    if a - int(a) == 0:
        return int(a)
    return a


while True:
    x = input("Number one: ")
    if x == "end":
        break
    try:
        x1 = float(x)
    except ValueError:
        print("incorrect input")
        continue
    y = input("Number two: ")
    if y == "end":
        break
    try:
        y1 = float(y)
    except ValueError:
        print("incorrect input")
        continue
    operation = input("Operation: ")
    if operation == "+":
        print("result:", int_check(x1 + y1))
    elif operation == "-":
        print("result:", int_check(x1 - y1))
    elif operation == "*":
        print("result:", int_check(x1 * y1))
    elif operation == "/":
        if y == 0:
            print("division by zero")
        else:
            print("result:", int_check(x1 / y1))
    elif operation == "end":
        break
    else:
        print("incorrect input")
        continue
    command = input("Want to end? Y/N: ")
    while command != "Y" and command != "N":
        print("incorrect input")
        command = input("Want to end? Y/N: ")
    if command == "Y":
        break
