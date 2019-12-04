---
type: slides
---

# Introduction

Notes: The goal of this chapter is to introduce to you - Type of Operators in Python and Various Statements such as Conditional and Iterative. 

So What you are waiting for? Let's get started.

---

# Operators in Python

- A Operator is a symbol (```+```,```-```,```**```, etc.) that's have specific meaning in Python.
- ```+``` means addition or concatenation, ```-``` means subtraction, ```**``` means raise to and 
so on.
- Types of Operators:
    - Arithmetic Operators (```+```,```-```,```*```,```/```)
    - Assignment Operator (```=```)
    - Relational Operators (```>```,```>=```,```==```,```<```,```<=```,```!=```)
    - Arithmetic Assignment Operator (```+=```,```-=```,```*=```,```/=```)
    - and many more.

---
# Arithmetic Operators

- Arithmetic Operators are used for performing arithmetic operations
- We have seen examples and usage of them in Chapter 1.

```python
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(10 / 2) # note the output of this statement
```

```out
4
0
4
5.0
```
---

# Assignment Operator

- Assignment Operator ```=``` is used to assign values to variables.
- Always remember that ```=``` works from Right to Left
- So, When we write ```a = 5``` i.e. assign the value of ```5``` to variable ```a```.

```python
a = 5 # this will work
print(a)
5 = a # this will not work and you will get your first error
# as you cannot assign value of variable a to 5.
```
```out
5
SyntaxError: can't assign to literal
```
---
# Relational Operators

- Relational Operators are used to perform comparison between variables / values.
- Kindly note that, Relational Operators return either ```True``` or ```False```.

```python
a = 23
b = 45
print(a > b)
print(a < b)
```
```out
False
True
```
---
# Relational Operators (contd.)

- There are other Relational Operators such as ```>=``` and ```<=```.
- ```>=``` returns ```True``` when a left side variable / value is greater than OR equals to right side variable / value, otherwise ```False```.
- ```<=``` works vice-versa.
- Check out the Exercise section for more practice on it.

```python
a = 23
b = 45
print(a >= b)
print(a <= b)
a = 45
print(a >= b) # this will return True
```
```out
False
True
True
```
---
#Let's Practice