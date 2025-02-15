# ME 700 Assignment 1 Part 1
This assignment serves as an introduction to Python, Github, and good coding practices for mechanical computation.  This assignment is split into 3 parts: a warmup interacting with the bisection method, a first part working with Newton's Method, and a second incorporating an elastoplastic material model. This is the part that interacts with Newton's Method.

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)

[![codecov](https://codecov.io/gh/jacobpgarrett/ME700_Assignment1_P1/graph/badge.svg?token=p5DMvJ6byO)](https://codecov.io/gh/jacobpgarrett/ME700_Assignment1_P1)
[![tests](https://github.com/jacobpgarrett/ME700_Assignment1_P1/actions/workflows/tests.yml/badge.svg)](https://github.com/jacobpgarrett/ME700_Assignment1_P1/actions)
---

## Setup
To install this package, begin by activating miniconda

```bash
module load miniconda
```

Then, set up a mamba environment
```bash
mamba create --name newton python=3.12
```

And then activate said environment:
```bash
mamba activate newton
```

Double-check that the correct version of Python is installed
```bash
python --version
```

Ensure that pip is using the most up-to-date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

Create an editable install of the code:
```bash
pip install -e .
```

Then, you can run pytest to ensure proper code coverage:
```bash
pytest -v --cov=src/newton --cov-report term-missing
```

## Using tutorials
To load each tutorial, begin by navigating to the tutorials folder:
```bash
cd tutorials
```

Then, to run a tutorial, type:
```bash
python #(Name of Tutorial)
```
Fill in the name of tutorial with one of the five tutorials in the folder, tutorial1.py, tutorial2.py, tutorial3.py, tutorial_mech_1.py, or tutorial_mech_2.py.

## Tutorial 1
Tutorial 1 exemplifies Newton's method for solving the function $x^3=0$.  An initial guess of 1 is set.

## Tutorial 2
Tutorial 2 solves the system of equations $u+v=0$ and $u-v=0$.  An initial guess of [1, 1] is set.

## Tutorial 3
Tutorial 3 solves a system of 5 equations: $x+y+z+w+v=15$, $2x-y+3z-2*w+v=7$, $x+2y-z+w-3v=-4$, $3x-4y+2z+5w-v=12$, and $x-y-z+w+v=1$.  The initial guess is set to [1, 1, 1, 1, 1].

## Mechanics tutorial 1
The first mechanics tutorial solves the problem from ME 700 at Boston University that is used to introduce Newtown's method in 2D.  This problem wants to measure the horizontal and vertical deflection when a mass is subjected to a vertical force but is suspended by two springs of uneven stiffness.  A figure and the equations that are sovled for are below.  The initial guess is set to (1,1).  In these equations, $k_{AB}=100N/m$ is the spring constant for the spring connecting points A and B, $k_{BC} is the spring constant for the spring connecting points B and C, $l=10m$ is the unstretched length of the springs, and $F=0.1N$ is the force applied in the vertical direction.

![image](https://github.com/user-attachments/assets/af72c4d9-b2aa-43cf-9fc2-8b3b1cf3f234)
![image](https://github.com/user-attachments/assets/ca8a2ed1-8a3c-41b1-93a0-68477d6a05cf)


## Mechanics Tutorial 2
The second mechanics tutorial is a modified problem from ME 304 at Boston University, Thermodynamics.  In this example, there is a turbine with steam going through it.  Using conservation of energy, the velocity of the steam leaving the turbine can be found.  The equation for this problem is shown below.  Where $\cdot{W_{out}} = 6.52MW$ is the work done by the turbine, $\cdot{m} = 11.5kg/s$ is the mass flow rate, $h_1 = 3000\frac{kJ}{kg}$ is the enthalpy at the inlet, $h_2 = 2430\frac{kJ}{kg}$ is the enthalpy at the outlet, and $v_1=8m/s$ is the velocity of the steam at the inlet.  The energy balance solved is shown below:

![image](https://github.com/user-attachments/assets/2ba29d7f-3836-45c0-86ea-b321078f7334)

## Generative AI Use

In this assignment, the forms of Generative AI that were used were vsCode Copilot, which assisted in completing code and ensuring correct Python syntax, and Chat GPT, which assisted in Github and CodeCov integration.

## Contributing
Pull Requests are welcome

## License
[MIT](https://choosealicense.com/licenses/mit/)
