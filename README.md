# ME 700 Assignment 1
This assignment serves as an introduction to Python, Github, and good coding practices for mechanical computation.  This assignment is split into 3 parts: a warmup interacting with the bisection method, a first part that works with Newton's Method, and a second part incorporating an elastoplastic material model.

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)

[![codecov](https://codecov.io/gh/jacobpgarrett/ME700_Assignment1_P1/graph/badge.svg?token=p5DMvJ6byO)](https://codecov.io/gh/jacobpgarrett/ME700_Assignment1)
[![tests](https://github.com/jacobpgarrett/ME700_Assignment1_P1/actions/workflows/tests.yml/badge.svg)](https://github.com/jacobpgarrett/ME700_Assignment1/actions)
---

## Setup
To install this package, begin by activating miniconda

```bash
module load miniconda
```

Then, set up a mamba environment
```bash
mamba create --name bisection-env python=3.12
```

And then activate said environment:
```bash
mamba activate bisection-env
```

Double-check that the correct version of Python is installed
```bash
python --version
```

Ensure that pip is using the most up-to-date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

Then, navigate to the correct directory (warmup, Part 1, Part 2)

## Using warmup tutorials
To load each tutorial, type:
```bash
python #(Name of Tutorial)
```
Fill in the name of tutorial with one of the five, either Tutorial1.py or Tutorial2.py for simple examples of the bisection method, Tutorial3.py for an example where you can input different values for the bisection to occur, and Tutorial_Mech1.py or Tutorial_Mech2.py for examples derived from mechanics problems.

## Generative AI Use

In this assignment, the only forms of Generative AI that were used were vsCode Copilot, which assisted in completing code and ensuring correct Python syntax, and Google Gemini, which was a result when looking up specific Python functions and library implementation.

## Contributing
Pull Requests are welcome

## License
[MIT](https://choosealicense.com/licenses/mit/)
