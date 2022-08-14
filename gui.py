import logging
from cmath import sqrt
from tkinter import *
from tkinter.messagebox import *


def reduce(num: complex) -> complex|float|int:
    """reduce a number to its lowest datatype (complex -> float -> int)"""

    if not num.imag:
        num = num.real
    if str(num)[-2:] == ".0":
        num = int(num)
    return num + 0


def quadratic(a: complex, b: complex, c: complex) -> tuple[complex, complex]:
    """return the roots of ax² + bx + c = 0"""

    disc = sqrt(b**2 - 4*a*c)
    x1, x2 = (-b + disc) / 2*a, (-b -disc) / 2*a
    return reduce(x1), reduce(x2)


def solution() -> None:
    for i in range(3):
        if not coeffs[i].get().strip():
            showwarning("Empty Field", "All coefficients are required.")
            logger.warning("One or more coefficients found empty")
            return

        try:
            complex(coeffs[i].get())
        except ValueError:
            showerror("Invalid Input", "Please enter a number as input")
            logger.error(f"Invalid input found - {coeffs[i].get()}")
            coeffs[i].delete(0, END)
            return

    a, b, c = [reduce(complex(box.get())) for box in coeffs]

    if not a:
        showerror("Invalid Input", "Coefficient of x² cannot be Zero")
        logger.error("Attempt to input a = 0")
        return

    roots = quadratic(a, b, c)
    logger.info(f"quadratic({a}, {b}, {c}) -> {roots}")

    for i in range(2):
        roots_boxes[i].config(state=NORMAL)
        roots_boxes[i].delete(0, END)
        roots_boxes[i].insert(0, str(roots[i]))
        roots_boxes[i].config(state="readonly")


LOG_FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(
    filename="quad-equations-logs.log", level=logging.DEBUG, format=LOG_FORMAT
)
logger = logging.getLogger()

logger.info("Opened Quadratic Equation Solver")

root = Tk()
root.geometry("400x240")
root.title("Quadratic Equation Solver")
root.resizable(False, False)

Label(
    text="Get the Roots of the equation: ax² + bx + c = 0",
    width=55, bd=5
).place(x=0, y=0)

Label(text=" ".join((
    "Enter the coefficients a, b and constant c,",
    "which can be real or complex."
))).place(x=10, y=23)

Label(text="YOUR EQUATION:").place(x=10, y=45)
Label(text="YOUR SOLUTION / ROOTS:").place(x=10, y=137)
Label(text="x²   +").place(x=105, y=68)
Label(text="x    +").place(x=225, y=68)
Label(text="=    0").place(x=345, y=68)
Label(text="x₁ =").place(x=40, y=168)
Label(text="x₂ =").place(x=40, y=198)

coeffs = []
for i in range(3):
    coeffs.append(Entry(width=10, bd=2, cursor="xterm"))
    coeffs[i].place(x=(35 + i*120), y=70)

roots_boxes = [Entry(width=50, bd=2, state="readonly") for _ in range(2)]
roots_boxes[0].place(x=77, y=170)
roots_boxes[1].place(x=77, y=200)

Button(
    text="Get the Roots!", width=52, cursor="hand2", command=solution, bd=3
).place(x=10, y=100)

root.mainloop()

logger.info("Closed Quadratic Equation Solver \n")
