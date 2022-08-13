print("This program will calculate the Roots of given quadratic equation")
print("Roots of the equation: ax\N{SUPERSCRIPT TWO} + bx + c = 0 are given as:")
print(
    "x =",
    "(-b \N{PLUS-MINUS SIGN} \N{SQUARE ROOT}(b\N{SUPERSCRIPT TWO} - 4ac))",
    "/ 2a"
)

while True:
    a = eval(input("\nEnter coefficient of x\N{SUPERSCRIPT TWO} (a): "))
    if a == 0:
        print(
            "Coefficient of x\N{SUPERSCRIPT TWO}",
            "cannot equal 0 (a \N{NOT EQUAL TO} 0)"
        )
    else:
        break

b = eval(input("Enter coefficient of x (b): "))
c = eval(input("Enter constant term (c): "))
D = b**2 - 4*a*c
nums = [a, b, c, D]

for i in range(4):
    if not nums[i].imag:
        nums[i] = nums[i].real

    if str(nums[i])[-2:] == ".0":
        nums[i] = int(nums[i])

a, b, c, D = nums

sign1 = "+" if isinstance(b, complex) or b >= 0 else ""
sign2 = "+" if isinstance(c, complex) or c >= 0 else ""

equation = f"{a}x\N{SUPERSCRIPT TWO} {sign1} {b}x {sign2} {c} = 0"

print("\nThe equation you entered is", equation)
print("Discriminant: D = b\N{SUPERSCRIPT TWO} - 4ac =", D)

x1, x2 = (-b + D**0.5) / (2*a), (-b - D**0.5) / (2*a)

if b == c == 0:
    print("It has roots of zero")

if not any(
    {isinstance(a, complex), isinstance(b, complex), isinstance(c, complex)}
    ):
        if D > 0:
            print("It has real and distinct roots")
        elif D == 0:
            print("It has real and undistinct roots")
        else:
            print("It has complex and conjugate roots")
else:
    print("It has general complex roots")

print(f"\nRoots of the equation {equation} are: \n{x1} and {x2}")