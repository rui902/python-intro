# Python 101 - Crash Landing

-----

## In this class:
In the file `variables.py` you will find some practical examples of how variables work in Python.
Copy the code and run on your computer to see it in action.

Try using a REPL and create some variables yourself! (Read below for some information about the REPL)

-----

## Relevant information / theory
Once Python is installed, running `python` in the command line will open a "Real-Time Interpreter" 
(called "REPL" - **R**ead–**E**val–**P**rint **L**oop), 
allowing you to execute Python commands a single time 
(i.e. after closing the REPL, you'll have to type every command again, since there's no persistence usually).

_PS. Running `python` will start the default Python version, if you have multiple versions installed, 
use the correct binary (e.g. `python2` or `python3`)._


## Different ways to run Python:
- Interactive Python (Real-Time / REPL)
- Python Scripts
- Python Modules
- Python Apps


### Difference between Scripts, Modules and Apps:
- Interactive:
    - Useful for testing some code excerpts, testing something small, or running very simple commands.


- Scripts:
    - File with simple blocks of code to achieve small tasks/purposes 
      - (e.g. Automate a database backup or calling a Python module to download a YouTube video, among others)
    

- Modules:
    - Reusable scripts that can be imported in large applications
    - Helps to make larger applications become more organized and readable
    - Allow developers to test small logic blocks


- Applications:
    - Large applications that usually import a vast amount of modules (internal and external) and serve bigger purposes.
    - Usually, applications run in the background (i.e. Web apps, APIs, ML/DL training algorithms, etc.)
      - For comparison, Python scripts usually run only once and terminate after running the whole code
        - Even if a script is automatable (e.g. through a cron), it runs once and then stops completely.


### Running Python code:
To run a python file, simply open a terminal, navigate to the same folder as your script and run `python <script.py>`. 
The same logic of multiple Python versions applies here as well (e.g. `python3 <script.py>` or `python2 <script.py>`)

For more details, and running Python on Windows, [click here](https://realpython.com/run-python-scripts/)

For a little "advanced" note on adapting Python files for specific python versions,
[refer to this page](https://stackoverflow.com/a/19305076).


## Python Standards:
**Python Enhancement Proposals (PEPs)** are how the Python maintainers define how Python should be programmed.
There are many, mostly informative and boring, but here are the two most important ones that all beginners should read:
- [PEP 08 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) : All about the rights and wrongs!
- [PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/) : Worth reading! (3 minute read max)
