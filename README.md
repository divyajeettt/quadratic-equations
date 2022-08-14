# quadratic-equations

## About quadratic-equations

quadratic-equations is a tiny project that simply finds the roots of polynomial equations with degree 2 with real/complex coefficients.

*Date of creation of CLI:* `January 15, 2020` \
*Date of creation of GUI:* `September 27, 2020`

The driver files for this project are available both as a command-line interface and a graphical-user interface. \
While the CLI is a one-time run program, the GUI can be used multiple times in the single run. The GUI also creates logs of the equations solved and traces errors (through logging) as well.

## Edit the logging settings

To modify the level of the `logger`, modify:

```python
logging.basicConfig(
    filename="quad-equations-logs.log", level=logging.DEBUG, format=LOG_FORMAT
)
```

 on [Line 59](https://github.com/divyajeettt/quadratic-equations/blob/c2715567e830ceeb74212d61f58b6e162141a560/gui.py#L59) of `gui.py` to:
 
 ```python
 logging.basicConfig(
    filename="quad-equations-logs.log", level=LEVEL, format=LOG_FORMAT
)
 ```
 
 where `LEVEL` can be one of:
 - `logging.INFO`
 - `logging.DEBUG`
 - `logging.WARNING`
 - `logging.ERROR`
 - `logging.CRITICAL`

## Footnotes

- The project <b>only</b> supports equations of the type `ax² + bx + c = 0`, i.e. purely quadratic equations.
- The coefficient `a` of `x²` cannot be set equal to 0.

## Run

Clone the repository on your device and navigate to the folder.

To run the command-line interface, execute:

```
python3 cli.py
```

To run the graphical-user interface, execute:

```
python3 gui.py
```
