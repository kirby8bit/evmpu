import math

def calc_expression(a, b, c):
  return 2*pow(a, 3) + 4*pow(b, 2) - 5*c


def calc_sqrt(a = 0, b = 0, c = 0):

  if calc_expression(a, b, c) >= 0:
    return f"a, b, c: {a}, {b}, {c}, по умолчанию a = 0, b = 0, c = 0", math.sqrt(calc_expression(a, b, c))
  else:
    return f"a, b, c: {a}, {b}, {c},по умолчанию a = 0, b = 0, c = 0: 2·a^3 + 4·b^2 – 5·c < 0", None