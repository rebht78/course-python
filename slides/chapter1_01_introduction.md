---
type: slides
---

# Introduction to Python

Notes: Hi, I am Sohel. I am Sr. Assistant Manager at NJ Group. I like to develop web applications and
mentor to-be developers.

The goal of this chapter is to get you started in Python as quickly as possible.

---

# First Program in Python

```python
# Add 1 + 1 and print the output of the equation.
print(1 + 1)
```

```out
2
```

Notes: In this first program, We use ```print``` function in Python to print output on the screen.
We will be learning more about functions in subsequent chapters; just remember ```print``` is a function and it is used to print output on the screen.

In the parenthesis [```()```] of ```print``` function, We have passed ```1+1```. This is an expression and Python will add ```1``` with ```1``` and give us output as ```2```.

---

# Let's try some more printing

```python
# Print "Hello, Python" (without ") on the screen.
print('Hello, Python')
# Let's print some more
print(2 * 3.5)
```

```out
Hello, Python
7.0
```

Notes: We have used ```print``` function again but to print two different values. First value is ```Hello, Python``` is a sentence and Python has a specific term for that called ```str``` (for string). ```str``` is a collection of characters. Second value is ```2 * 3.5```, which gives us ```7.0``` as an output.

Also note that Python is case-sensitive. ```Print``` and ```print``` are two different functions.

---

# Comments

```python
# We have used comments earlier, too
# Comments & Basic Data Type
```

```out
No output is displayed.
```

Notes: Comments are like notes that you leave behind, They are ignore by the interpreter, meaning that you can write whatever you want, and the computer will ignore it. 

A good comment will be short, easy to read, and to the point.

In Python, we can write comments using the hash (#) symbol. Any text that follows this
symbol will be commented out.

---

# Multi-Line Comment

```python
"""
this is a
multi-line 
comment
"""
print('Hello, Python') # this is a single line comment
```

```out
Hello, Python
```

Notes: To write multiline comments so that you may write more descriptive paragraphs for
larger portions of code, we would need to use three opening and closing double quotes.
---

# Let's Practice