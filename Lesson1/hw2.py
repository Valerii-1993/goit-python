import math
print ('решаем ax^2 + bx + c = 0')
a = float(input('Введите число для a: '))
print ('Ok')
b = float(input('Введите число для b: '))
print ('Ok')
c = float(input('Введите число для c: '))
print ('Ok')
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корни отсутствуют")