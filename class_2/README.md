# Functional Programming in Python

-----

## In this class:
In the file `functional_programming.py` you will find some practical examples of how 
create functions, call functions, pass arguments and manipulate its parameters.

In the `scripting` folder you will find some examples scripts. 
Check the `README.md` to learn how to run a single script and how to import a script into another one.

In the `modules` folder you will find a some example scripts, which are acting as modules. 
Check the `README.md` to learn how to run them as a module, and how to configure this setup.

Copy the code and run on your computer to see it in action.

Try using a REPL and play around!

-----

## Relevant information / theory

### Functions
A function in programming is a specific block of code that can be called (executed) multiple times, 
and has the ability to receive variables as parameters for each call, 
allowing the same code to yield different results without needing any change.

The keyword `def` introduces a function definition. 
It must be followed by the **function name** and the **parenthesized list of formal parameters**. 
The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; 
this string literal is the function’s **documentation string**, or **docstring**.
There are tools which use docstrings to automatically produce online or printed documentation, 
or to let the user interactively browse through code; 
it's always a good practice to include docstrings in code that you write, so make a habit of it!

Here's an example of a simple function, involving the previous statements:
```python
# function that writes the Fibonacci series up to number `n`
def fib(n):
    """Prints the Fibonacci series up to n."""
    
    a, b = 0, 1
    
    while a < n:
        print(a)
        a, b = b, a+b

# Now call the function we just defined:
fib(10)

# Prints:
# 0 
# 1 
# 1 
# 2 
# 3 
# 5 
# 8
```

Please refer to the [official documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) 
for a deeper dive into functions.

#### Returning values
The function of the `return` keyword is the same as pretty much any other programming language. 
Any function can be called and return some given value.

Returns are not required when defining functions, although they are encouraged.

By default, any function returns `None` when it finishes executing, **unless** an explicit `return` statement is found.

For more details on returning values and default behaviors, 
check [this article](https://realpython.com/python-return-statement/)!

##### Complex returns
Additionally, there are many times when return statements are complex.

The article previously used has two topics really well covered that I'd love to mention:
- https://realpython.com/python-return-statement/#using-return-with-conditionals
- https://realpython.com/python-return-statement/#returning-true-or-false

#### Arguments and Parameters
For the main idea of Arguments vs Parameters, 
the editors behind the [official documentation](https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter) 
did a great job at explaining the difference.

On function definitions, we have a list of arguments.
These can be of two kinds: "Positional Arguments" and "Keyword Arguments".

Dominating them is a little advanced for this course, but to know more on how to use them, 
refer to the [official documentation](https://docs.python.org/3/glossary.html#term-argument).

### Lambda Expressions!
Small anonymous functions can be created with the lambda keyword. 
This example is a function that returns the sum of its two arguments: 
`lambda a, b: a+b`. 

Although one can assign lambda to a variable and use them like functions, it's highly discouraged.
PEP8 states the following:

> Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier:
> ```python
> # Correct:
> def f(x): return 2*x
> 
> # Wrong:
> f = lambda x: 2*x
> ```


Based on [this answer](https://stackoverflow.com/a/25010243) from StackOverflow,

"Assigning lambdas to names basically just duplicates the functionality of def - and in general, 
it's best to do something a single way to avoid confusion and increase clarity. [...]
In general, the main argument against doing this is that def statements will result in more lines of code. 
My main response to that would be: yes, and that is fine. 
Unless you are code golfing, minimising the number of lines isn't something you should be doing: 
go for clear over short."

Take a look at the following example, where lambda usage is encouraged:
```python
# Sorts the elements of `some_list` using the key "key1" as the sorting "source"
some_list = [{"key1": "B", "key2": "1A"}, {"key1": "A", "key2": "2B"}]
sorted(some_list, key=lambda elem: elem["key1"])
```

In short, Lambda functions can be used wherever function objects are required.
They are syntactically restricted to a single expression. 
Semantically, they are just syntactic sugar for a normal function definition.
Like nested function definitions, lambda functions can reference variables from the containing scope.

Please refer to the [official documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
for more details on Lambda expressions.


### Generators
The following are brief explanations/examples of generators.
For more details on generators, 
refer to the [official documentation](https://docs.python.org/3/glossary.html#term-generator).

#### Generator (or "Generator function")
A function which returns a generator iterator. 
It looks like a normal function except that it contains `yield` expressions, instead of `return`, 
producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.

Usually refers to a **generator function**, but may refer to a **generator iterator** in some contexts. 
In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

#### Generator iterator
An object created by a Generator Function.

Each `yield` temporarily suspends processing, remembering the location execution state 
(including local variables and pending try-statements). 
When the generator iterator resumes, it picks up where it left off 
(in contrast to a function which start fresh on every invocation).

#### Generator expression
An expression that returns an iterator. 
It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. 

The following combined expression generates values for an enclosing function:
```python
sum(i*i for i in range(10))  # sum of squares 0, 1, 4, ... 81
# returns: 285
```


#### List comprehensions
Two common operations on an iterator's output are:
1. Performing some given operation for every element
2. Selecting a subset of elements that meet some condition

For example, given a list of strings, you might want to strip off trailing whitespace from each line 
or extract all the strings containing a given substring.

List comprehensions and generator expressions (short form: "listcomps" and "genexps") 
are a concise notation for such operations, borrowed from the functional programming language Haskell.

You can strip all the whitespace from a stream of strings with the following code:
```python
line_list = ['  line 1\n', 'line 2  \n', ...]

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
```

You can select only certain elements by adding an "if" condition:
```python
line_list = ['  line 1\n', 'line 2  \n', ...]
stripped_list = [line.strip() for line in line_list if line != ""]
```

With a list comprehension, you get back a Python list; 
`stripped_list` is a list containing the resulting lines, not an iterator. 

**Generator expressions return an iterator that computes the values as necessary, 
not needing to materialize all the values at once.** 

**This means that list comprehensions aren’t useful if you’re working with iterators that return an infinite stream 
or a very large amount of data. Generator expressions are preferable in these situations.**

Generator expressions are surrounded by parentheses `()` and list comprehensions are surrounded by square brackets `[]`.

For more details, please refer to the 
[official documentation](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions).


### Decorators
A decorator in Python is a function that takes another function as its argument, and returns yet another function. 
Decorators can be extremely useful as they allow the extension of an existing function, 
without any modification to the original function source code.

Decorators are really cool to learn, but they're also pretty advanced for this course, 
so here are a few relevant links if you want to learn more about them:
- https://peps.python.org/pep-3129/
- https://docs.python.org/3/reference/compound_stmts.html#function
- https://docs.python.org/3/reference/compound_stmts.html#class-definitions
- https://towardsdatascience.com/how-to-use-decorators-in-python-by-example-b398328163b

