# python-intro
Introduction to Python - a short course

Hosted by [NEI-ISEP](https://github.com/Nucleo-Estudantes-Informatica-ISEP)

Contents by [Rui Costa](https://github.com/rui902)


------

To better follow the examples and demos, Python 3.8 is recommended. 
Please refer to the [installation section below](#installing-python).

All the code has been tested in Ubuntu 20.04.4 LTS (Linux 5.13.0-30-generic; x86-64).
Other Linux versions, as well as macOS and Windows, haven't been tested yet, but all should work properly in most cases.

_If you find any error or have any questions/suggestions, feel free to reach out to me using my email._

_*(Some contents are not yet available, and some topics need to be completed (marked below as TBC), 
but will soon be added here. Follow/Star this repository to be notified and keep updated!)_

------


## Course Contents:

____
_**Important Note:** Make sure to always go through each README file inside each the classes folders, 
they will contain things like comments, context, theory and relevant background information 
that are sometimes too long to fit in the practical examples, 
but very important to understand why sometimes Python behaves in specific ways or how it compares to other languages._
____

### Class 0: Basic introduction **(TBC)**
- Python Introduction
  - History
  - Python REPL (**R**ead–**E**val–**P**rint **L**oop)
    - iPython
  - Running Python scripts
  - PEPs and Conventions
- Basic variable types
  - Strings
  - Ints
  - Floats
  - Booleans
  - Null values
- Type Casting in Python


### Class 1: Final baby steps **(TBC)**
- Data Structures in Python
  - Lists, Tuples, Sets and other Sequences
  - Dictionaries
- Iterable protocol
  - Iterables and Iterators
- Flow Control in Python
  - Loops
    - While
    - For
  - Conditionals
    - if/elif/else
- Operators in Python
  - Conditionals:
    - And
    - Or
    - Not
  - Comparison
    - Is
    - greater than, less than, etc.
- Mutability
  - Difference between mutable and immutable objects
  - Hashing

### Class 2: Functional programming and other cool things **(TBC)**
- Functions
  - Definition
  - Parameters and Arguments
  - Advanced Parameters
    - Default values
    - Positional and Named Arguments
    - *args, **kwargs, and unpacking
  - Lambdas / anonymous functions
  - Returning values
    - Yielding values (_see generator functions below_)
  - Decorators
- Generators
  - Generator functions
  - Generator iterators
  - Generator expressions (e.g. Comprehensions)
    - General expressions
    - List comprehensions
    - Dict Comprehensions
- Standard library
  - Importing and using standard library modules
- Scripts vs Modules
  - Defining scripts vs defining modules
  - Difference when importing and using both
  - \_\_name\_\_ and why it's so commonly used in Python
  - Default importing behaviors in Python and how to avoid common issues


### Class 3: Object-Oriented Programming (OOP) Basics **(TBC)**
- Introduction to classes in Python
  - Defining a class
  - Defining class attributes and default values
  - \_\_init\_\_ and Python constructors
  - Defining class methods
  - self/cls difference and usage
  - Defining Static Methods
  - Public and Private attributes/methods in Python
  - Documenting Classes and Methods
  - Operator Overloading in Python
    - Default ("Available") class-function overloading (e.g. \_\_repr\_\_
- Exceptions
  - Raising Exceptions
  - Handling Exceptions
- Using requirements.txt to manage dependencies
  - Installing all dependencies using pip


### Class 4: More on classes and Unit Testing **(TBC)**
- Continuing Classes and OOP in Python
  - Inheritance and Implementations; Polymorphism; 
  - Modularity and logic separation
- Passing custom functions as parameters
- Unit Testing
  - Installing and testing Python code with Pytest


### Class 5: Python + Databases **(TBC)**
- Interacting with Databases in Python
  - Introduction to common databases (i.e. SQLite, MySQL and PostgreSQL)
  - Installing and importing public packages from Pypi using pip for easier development
  - Connecting and interacting with tables and records
- Configurations
  - Using config files to improve readability and easier development
  - Organizing specific configurations for different environments in the config files
  - Getting values from the configuration when using specific environments
- Connections
  - Multiple ways to define connections and manage db connections
    - Suggestions and "Best Practices"
- Database interaction
  - DB Queries: Inserting, Selecting, Updating and Deleting records
  - Some examples of different Cursors available in each database
  - Closing the connections


### Class 6: Web and API development **(TBC)**
- TBC
  - API Development using Flask and Django frameworks
  - Intro to Web Development using Django framework


### Class 7: Tips and Tricks **(TBC)**
  - Preparing to build large projects and working in teams
    - Organizing your code
    - Installing and using .env in your projects 
  - Managing large existing projects
    - Installing multiple complex dependencies
  - Configuration versatility
    - More on .env configurations and public/private configuration management
    - Yaml configuration and other config alternatives
    - Passing console arguments and automating script execution
      - Standard System arguments vs Argparse module
    - All about Logging
      - Tips and tricks on how to use logging like a pro
        - Log formatting
        - Coloring logs for the console
        - File logging and other ways to manage logs for large scales
          - Size-based and Time-based file rotations
  - _Dockerizing_ Python scripts and projects (_No introduction to docker whatsoever_)


### Class 8: Honorable mentions **(TBC)**
- Honorable mentions
  - Common Frameworks
  - Personal opinion on frameworks/projects compared in the past by experience
  - Other interesting project mentions


-----


## PEP links:
Recommended:
- [PEP 8   -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 20  -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

Interesting/Mentioned:
- [PEP 263 -- Defining Python Source Code Encodings](https://www.python.org/dev/peps/pep-0263/)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)


## Other Links:
### Recommended Python Tutorials: 
- https://pythonprogramming.net/ (Python Basics, Web Development, AI & Data Analytics, etc)
- https://pythonprogramming.net/introduction-learn-python-3-tutorials/ (Python 3 introduction by Sentdex)

### Personal recommended ("prefered") articles/blogs/pages
- https://docs.python.org/ (Incredible documentation, explanations and examples)
- [The StackExchange network](https://stackexchange.com/sites#technology) (Q&A)
  - _Mainly [StackOverflow](https://stackoverflow.com/)_ (Q&A / Code samples)
- https://pythonprogramming.net/ (Tutorials mostly)
- https://realpython.com/ (Tutorials mostly, but also articles)
- https://www.tutorialspoint.com/python/index.htm (Tutorials mostly)
- https://www.reddit.com/r/Python/ (News and Q&A)
- https://www.geeksforgeeks.org/ (Articles mostly)
  - https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/ (Tutorial)
- https://www.digitalocean.com/community/tags/python (Articles mostly, a few things specifically for Python)

### Recommended online courses
- https://www.pluralsight.com/search?q=python (Online Courses, other technologies as well!)
- https://www.udemy.com/topic/python/ (Online Courses, other technologies as well!)
- https://www.kaggle.com/learn/python (Online courses and tech challenges)

-----

## Installing Python
Installing Python 3.8.5 in Windows / macOS:
1. Open: https://www.python.org/downloads/release/python-385/
2. Scroll to "Files", and download the recommended installer for your system 

If you're not sure which one to choose, these are the most likely you're looking for:
- **Windows:** 
  - "Windows x86-64 executable installer" (for 64 bit systems, most likely)
  - "Windows x86 executable installer" (for 32 bit systems, least likely)
- **MacOS:** 
  - "macOS 64-bit installer"
- **Linux:** 
  - Most Linux distros and versions come with Python pre-installed, but Google is your best friend here!

There are lots of Youtube tutorials for each system, and also Google is very helpful, if you still have any questions :)

_PS. If you don't have Python 3.8 installed, 
you can either install an alternative version (and use two versions at the same time in your system),
or instead follow through the examples and let me know if you need help with a different Python version. 
I'll try adapting examples for that Python version on a different branch!_

-----

## Recommended IDEs for Python programming
Personally, I recommend PyCharm IDE from JetBrains. 
There is a [Pro, Community and EDU version available](https://www.jetbrains.com/pycharm/).

Before Pycharm, for small projects and quick scripting, 
I got really used to [Sublime Text](https://www.sublimetext.com/) 
(and loved using it for pretty much everything involving text writing and text manipulation). 
I stopped using it because it's not really an IDE and although being great, 
I really needed some extra features it was lacking.

Any other IDE/Editor that has Python plugins could be used as well, 
and the only others I tried in the past that I can recommend are 
[VS Code](https://code.visualstudio.com/) and [Atom](https://atom.io/).
