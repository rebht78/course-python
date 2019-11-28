---
type: slides
---
# Basic Data Types

Notes: When we write programs, we need to store data. Data are of various types. As for example: Student's Name, Percentage, Student ID, etc. Name is a series of Characters, Percentage is a real number - fancy way to say number has decimal point, ID is a whole number.

In this section, We will learn how Python deals with data type.
---
# Strings

- A _String_ is a series of characters.
- Anything inside quotes is considered a string in Python
- You can use single quote (') or double quotes (") around your strings.
---
# Example of Strings

```python
episode_name1 = 'A Study in Pink' # this is a string with single quote
episode_name2 = "The Blind Banker" # this is a string with double quotes
print(episode_name1)
print(episode_name2)
```

```out
A Study in Pink
The Blind Banker
```
---
# Operations on Strings - Index

- Strings are indexed.
- That means, you can access individual character of the string by using a number.
- In Python, index starts from zero.
- Hence, a string's first character has a zero index.

```python
episode_name = 'A Study in Pink'
print(episode_name) # this will print A Study in Pink
print(episode_name[0]) # this will print first character of the string i.e. A
```

```out
A Study in Pink
A
```
Notes: To access the first character on the string you created, use variable name with index 0 within square brackets as shown in the code.
---
# Operations on Strings - Index (contd.)

- You can access other characters by simply specifying their indices.
- You can also use negative index in Python.
- Negative index starts from -1

```python
episode_name = 'A Study in Pink'
print(episode_name) # this will print A Study in Pink
print(episode_name[3]) # this will print fourth character, space are counted.
print(episode_name[-1]) # this will print last character, k
print(episode_name[-4]) # this will print - P
```

```out
A Study in Pink
t
k
P
```
---
# Operations on Strings - Concatenation

- It is important to understand what you can do with string data types.
- To concatenate strings, I mean that We want to add one string to the end of another.

```python
first_name = 'Sherlock'
last_name = 'Holmes'
full_name = first_name + ' '+ last_name # note the space between first_name and last_name
print(full_name)
```
```out
Sherlock Holmes
```
---
# Let's Practice
