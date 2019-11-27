---
type: slides
---
# Basic Data Types

Notes: When we write programs, we need to store data. Data are of various types. As for example: Student's Name, Percentage, Student ID, etc. Name is a series of Characters, Percentage is a real number - fancy way to say number has decimal point, ID is a whole number.

In this section, We will learn how Python deals with data type.
---
# Strings?

- A _String_ is a series of characters.
- Anything inside quotes is considered a string in Python
- You can use single quote (') or double quotes (") around your strings.
---
# Example of Strings?

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

Notes: Take note that when you are declaring a variable, you are not stating that the variable
```first_variable``` is equal to 23. What the statement actually means is “assign the value of ```23``` to ```first_variable```”.
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
print(episode_name[-1]) # you can also use negative index
```

```out
A Study in Pink
A
k
```
---
# Let's Practice

