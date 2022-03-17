# Python 101 - The last baby steps

-----

## In this class:
In the file `more_on_python.py` you will find some practical examples of how 
Data Structures, Operators, Conditions and Loops work in Python.

Copy the code and run on your computer to see it in action.

Try using a REPL and play around!

-----

## Relevant information / theory

### Data Structures
Please refer to [this page](https://docs.python.org/3/tutorial/datastructures.html) 
for more details and examples about the Data Structures in Python.

Some Data Structure types in Python are:
- Lists
  - Stacks
  - Queues
- Tuples
- Sets
- Dictionaries

#### Lists
Lists are pretty much the equivalent of the Arrays in other languages, 
and allow developers to work with lists of elements of any data type 
(e.g. a single list variable can have Strings, Ints, Null values and even other lists!).

_PS. Lists are mutable, meaning that its value may be changed over time._

##### Tuples
While lists and strings have many common properties, such as indexing and slicing operations, 
they are two examples of sequence data types 
(see [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq)). 

Since Python is an evolving language, other sequence data types were eventually added. 
The standard sequence data type being the Tuple.

Tuples are immutable sequences, typically used to store collections of heterogeneous data 
(such as the 2-tuples produced by the `enumerate()` built-in). 
Tuples are also used for cases where an immutable sequence of homogeneous data is needed 
(such as allowing storage in a set or dict instance).

If you're curious, and need a deeper understanding on how the tuples "immutability" work in Python, 
please refer to the following topics on StackOverflow:
- https://stackoverflow.com/a/9756028
- https://stackoverflow.com/a/26262881
- https://stackoverflow.com/a/26262928


#### Sets
A Set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

#### Dictionaries
One of the most useful data types built into Python is the dictionary.
Dictionaries are sometimes found in other languages as "maps", "associative memories" or "associative arrays". 

Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, 
which can be any immutable type; strings and numbers can always be keys. 
Tuples can be used as keys if they contain only strings, numbers, or tuples; 
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
You can't use lists as keys, since lists can be modified in place.

It is best to think of a dictionary as a set of key:value pairs, 
with the requirement that the keys are unique (within one single dictionary). 

A pair of braces creates an empty dictionary: {}. 
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; 
this is also the way dictionaries are written on output.

### Iterables and Iterators
The terms `iterable` and `iterator` are often (and wrongfully) used interchangeably in order to describe 
an object that supports iterations, that is an object that allows to iterate over its elements/values.
In Python, they are two completely distinct concepts that are usually a source of confusion, especially for newcomers.

The iteration protocol is a protocol used by all iteration tools in Python 
and implemented by loops, comprehensions, maps, etc. 

In short, both can be explained using two distinct objects:
- The `iterable` is the one that allows you to iterate over its elements
- The `iterator` is the one that produces the values during the iteration (it's also returned by the iterable object)

Strings, Lists, Tuples, Dictionaries, Sets all implement the Iterable protocol, 
allowing us to iterate over its elements/contents.

Please refer
[to this, very well-written, article](https://towardsdatascience.com/python-iterables-vs-iterators-688907fd755f) 
for more details on how iterables and iterators work!


### Operators
Please refer to [this page](https://docs.python.org/3/library/operator.html) 
for more details and examples about the built-in operators in Python.

#### Comparison operators
Some Python operators include (assume "a" and "b" are defined variables):
- `a == b` : compares if variables a and b have the same values [*1]
- `a != b` : compares if variables a and b have different values [*1]
- `a > b`  : compares if variable a has a value bigger than b's value
- `a < b`  : compares if variable a has a value lower than b's value
- `a >= b` : compares if variable a has a value bigger or equal to b's value
- `a <= b` : compares if variable a has a value lower or equal to b's value

To compare if a variable has a Null value, it's common to use the `is` keyword, as follows:
`a is None`.

Using `a == None` is discouraged.

_[*1] compares the value of the variables, although they may be the same variable. 
To compare if both variables are exactly the same use `a is b` instead 
(i.e. compares if they are the same object in memory)._


## Flow Control
Operators are commonly used in flow control's condition.

Python uses the `if (condition):`/`elif (condition):`/`else:` nomenclature.

_Note: `elif` and `else` are optional._

_Note: parenthesis are also optional surrounding the conditional expressions._

The part that comes after the `if`/`elif` is called the condition, it must contain at least one expression, 
although multiple expressions can be used. 
The expressions inside must always return a boolean value.

if the expression doesn't return an explicit boolean value, 
Python's interpreter will cast the expression result to a boolean value.
As mentioned on Class 0, empty strings (""), 0 and None are also considered "falsy" values and are cast to `False`.

All other values are expected to be true values, unless a few exceptions on complex variables and expressions.

### !! Indentation example !!
In the context of this course, here's the first example how indentation works in Python.
After the flow control's conditions, it's required to add some expression/behavior following the 
[PEP8 definition](https://peps.python.org/pep-0008/#indentation), 
check the `if-statement` example for some basic examples.

### Negating an expression
To negate an expression, Python uses the `not` keyword, although `not` may be used in two different ways:
- `not (expression)` - negates the entire expression (note: parenthesis are not required in this use case)
- `a is not b` - together with another built-in keyword to negate its value

### Test value/contents
When checking if a variable has a true value, just use the variable name with nothing else:
- e.g. `if a:` - if `a` doesn't contain a falsy value, this will always return True
- e.g. `if not b:` - if `b` has a falsy value, then this will return True

This is useful when working with dynamic values, such as comparing if a string is empty 
(i.e. doesn't require checking how many characters it has, of if the variable is Null, for example).

### Combining expressions in the condition
We can combine multiple expressions using `and` and `or` operators, 
and unlike other programming languages, parenthesis help for readability but are not required, 
meaning the following statements are equivalent:
- `if x > 0 and x < 10:` 
- `if (x > 0 and x < 10):`

PS. For the specific example above (checking if x is between two numbers), 
the following statement is recommended instead:
`if 0 < x < 10:`

Combining expressions with both these operators
[may frequently yield "weird" results](https://peps.python.org/pep-0308/).
For complex conditions, it's always a good idea to use parentheses `(` and `)`. 
Sometimes they're required to change Python's order of operations. 
And at most times they simply make code easier to understand.

[This Web Article](https://kodify.net/python/if-else/if-conditions/) sums up pretty well these scenarios.


## Loops
There are two main ways to loop around iterables, the built-in `while` loop and `for` loop.

### While Loop
A simple example of how to use the While loop is to write an initial sub-sequence of the Fibonacci series as follows:
```python
# Fibonacci series:
# the sum of two elements defines the next
a = 0
b = 1
while a < 10:
    print(a)
    a = b
    b = a+b

# Results in:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
```

Similarly to the flow control expressions, 
while loops will run the "body" until that expressions yields a False value.

In the above example, the while loop will keep running and printing the Fibonacci sequence 
until the value of `a` becomes greater than 10.

### Infinite Loops (!)
If the condition never evaluates to False, then we will have what's called an infinite loop. 

In theory, an infinite loop never stops,
unless without external intervention or all the machine's resources have been exhausted.
Make sure infinite loops never happen except if programmed on purpose.

For more information about infinite loops, and examples of how they are sometimes rightfully used, 
refer to [this article](https://realpython.com/python-while-loop/#infinite-loops), 
as well as [this one](https://www.freecodecamp.org/news/python-while-loop-tutorial/)!

### Manipulating the loop's execution - The `continue` and `break` keywords
Let's assume that the body of the loop has some complex conditions.

If the very first condition isn't met, instead of placing the rest of the code in the `else` block, 
we can use the `continue` keyword, making the code go back to the condition and "restarting" the loop from the top.

If some other condition is met, we can completely jump out of the loop without having to run the rest of the code.

Here's a quick example:
```python
# Seemingly infinite loop with continue and break
a = 0
while True:
    print(a)
    a = a + 1
    
    if a < 10:
        continue

    # whenever `a` has a value below 10, the loop never reaches this line and below
    # -----
    # the following lines are only interpreted/executed when the value of `a` is 10 or above
        
    if a >= 11:
        break

    # This next statement should only run once, 
    # since the above condition will halt the loop (using `break`) as soon as `a` has a value of 11
    print("This statements runs only once when `a` has value of 10:", a)
```

To demonstrate how `continue` affects readability, 
the alternative (below) for the above example seems very simple as well, 
but would bring a lot of unnecessary complexity if there was more code in each condition.

Besides, if there's any additional code after the `if` block, the interpreter will always run it unnecessarily!
```python
# Seemingly infinite loop with break but no continue
a = 0
while True:
    print(a)
    a = a + 1
    
    if a < 10:
        print("prints this everytime, while a's value is below 10!")
        
    elif a >= 11:
        break
    
    else:
        print("This statements runs only once when `a` has value of 10:", a)
```

### The most useless keyword in Python: `pass`
Usually, when writing code, sometimes we either comment some line of code, and the block becomes "empty".
Since Python has some "programming rules" on indentation, after an `if` or `while` block (and some other cases), 
it's required to have at least one expression.

When necessary, we can simply put a useless `pass` statement inside, 
which will be evaluated and "allow that rule to be validated".

Here's a few examples:
```python
# Flow control example
if True:
    pass

elif False:
    pass

else:
    pass


# While loop example
# important note!!
# this will keep the computer running the pass command over and over again since the condition is never False!
while True:
    pass
```

Please refer to the [official documentation](https://docs.python.org/3/tutorial/controlflow.html#pass-statements) 
for more details.


### For Loop
The for statement in Python differs a bit from how it's used in C or Pascal for example. 
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), 
or giving the user the ability to define both the iteration step and halting condition (as C), 
Python's for statement iterates over the items of any sequence, in the order that they appear in the sequence. 

Please refer to the [official documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements) 
for a more detailed demonstration and examples.

_PS. Please note the pun they **definitely** intended when giving their first example!
`For example (no pun intended)` :)_

The `for` expects the following syntax:
```python
for (variable) in (iterable):
    pass
```

Check the official documentation above for more details on how to work with the for statement,
for now, this will be the only simple examples:
```python
some_string = "abcdefg"
for letter in some_string:
    print(letter)

# (should print above all the letters, line by line)


some_int_list = [1, 2, 3, 4, 5]
for number in some_int_list:
    print(number)

# (should print above all the numbers, line by line)


# remember sequences may contain different data types
some_random_list = [True, 5, "String", {"key": "value"}, None]
for element in some_random_list:
    print("Element: {}\nType: {}\n".format(element, type(element)))

# Prints the following:
# 
# Element: True
# Type: <class 'bool'>
# 
# Element: 5
# Type: <class 'int'>
# 
# Element: String
# Type: <class 'str'>
# 
# Element: {'key': 'value'}
# Type: <class 'dict'>
# 
# Element: None
# Type: <class 'NoneType'>
# 
```




















