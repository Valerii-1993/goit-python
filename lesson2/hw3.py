while True:
    x = (input("Enter number: "))
    try:
        x = float(x)
    except ValueError:
        print(f"your {x} is not a number")
    else:
        break

while True:
    z = input("Enter the operant +-*/= : ")
    while z not in "+-*/=" or z == "":
        z = input("It`s not operant: ")
    if z == "=":
        break

    while True:
        y = (input("Enter number: "))
        try:
            y = float(y)
        except ValueError:
            print(f"number {y} is not a number")
        else:
            break

    if z == "+":
        x += y

    elif z == "-":
        x -= y

    elif z == "*":
        x *= y

    elif z == "/":
        
        while y == 0:
            try:
                x /= y
            except ZeroDivisionError:
                print("Zero Division Error")
                y += float(input("Enter the number: "))
            else:
                break

        x /= y

print(float(x))