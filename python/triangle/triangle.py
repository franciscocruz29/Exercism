def valid_triangle(f):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and f(sides)
    return inner

@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1

@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3

@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3

""" def is_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


def equilateral(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) == 3 """
