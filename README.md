# Problems: katas on [Codewars](https://www.codewars.com)
## A very basic custom test suite for competitive programming.

**TLDR**:  Execute ```python driver.py ProblemA``` to test the solution to `ProblemA` against all the test cases.

### Some instructions.

#### For writing the solution:
- (Optional): Source into `venv` so `numpy` and `scipy` are accessible.
- Copy `template.py` into `/solutions` and rename it.
- Filename should be one-word.
    1. Example: `ProblemA.py`
-  This one's important: **Write the solution in the** `solve()` method
    inside `problemA.py`.
- Make sure the drivers return the result in `ProblemA.py`.

#### For testing the solution:
-   Fill in the input for test cases `1, 2, ...` by creating `ProblemA1.in, ProblemA2.in, ...`
    inside `data/input`.
-   Fill in the expected output for test cases `1, 2, ...` by creating `ProblemA1.out, ProblemA2.out, ...`
    inside `data/output`.
-   To execute all the tests, simply execute `python driver.py ProblemA` in the shell.


---
## List of Problems Solved:

- **\(5 kyu\)** [Directions Reduction](https://www.codewars.com/kata/550f22f4d758534c1100025a) : [Solution](solutions/Direction.py)
- **\(5 kyu\)** [Prime Operations](https://www.codewars.com/kata/58a3e2978bdda5a0d9000187) : [Solution](solutions/Primeoperations.py)
