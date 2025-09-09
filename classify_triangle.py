def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return "InvalidInput, side can not be negative or zero"
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        traingle = "Isosceles"
    else:
        traingle = "Scalene"

    # sides = sorted([a, b, c])
    # if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
    #  return traingle + "Right"

    return traingle


if __name__ == "__main__":
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    print("Triangle is:", classify_triangle(a, b, c))
