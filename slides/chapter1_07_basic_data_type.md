---
type: slides
---
# Basic Data Types - Numbers

---
# Numbers

- _Numbers_ are quite often used in programming.
- You need numbers to store marks of students, salary of employees, etc.
- Python treats numbers in two different ways:
    - Integers (_int_)
    - Floats (_float_)
---
# Example of Numbers

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
# Let's use two **

```python
print(5 ** 2) # ** is used for exponent
print(2 ** 5)
```

```out
25
32
```
---
# Order of Operations

```python
print(2 + 3 * 5)
print((2+3) * 5)
```

```out
17
25
```
Notes: Python supports the order of operations -  you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.
---
# Floats

- Python supports real numbers (with decimal point) and calls it a _float_.

```python
print(3.14 + 221)
print(3.14-1.11) # observe this statement's output
print(2 * 0.2)
```
```out
224.14
2.0300000000000002
0.4
```
---
# How to identify data type of a value?

- You can use ```type()``` function to identify data type of a value or variable.

```python
house_no = 221
address = 'Baker Street'
carpet_area = 120.35

print(type(house_no))
print(type(address))
print(type(carpet_area))
```
```out
int
str
float
```
---
# Let's Practice
