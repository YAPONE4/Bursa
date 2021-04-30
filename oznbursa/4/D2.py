import math

def formulaM(x, y, a, d):
    return(math.sin(x + 2 * y) / (math.fabs(x - math.pow(math.e, a * x * y))) + 0.3 * math.pow((x - ((a + 4.2) / (d * y))), 1 / 3) + math.log(a * x * x, 5))

def formulaZ(x, y, k):
    return(math.log1p(x) + math.pi * math.atan(y * y) + math.tan((k * x) / 2))

print(formulaM(1, 2, 3, 4))
print(formulaZ(1, 2, 3))