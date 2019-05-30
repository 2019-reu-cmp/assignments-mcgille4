# Python Basics: Part 2

Chris Seymour

May 30, 2019

---

## Learning Goals

1. Get files via `git`.
2.  Be able to run and understand basic code
3. Be able to explain what is and how *control flow* works in python
4. Understand the similarities and differences in the basic python collection types
5. Learn 10 more Python terms.

---

## Git and GitHub

- Get a Github account
- Go to Github classroom link, from website
- GitKraken
- Log in and clone your new repo
- clone the assignments repo
- copy files to your repo's directory
- `commit` your changes with a message
- `push` the changes to the server

<!-- 1. Get files via `git`. -->

---

## modifiers

make changes to a variable
equivalent to  `x = x + 1`
```
x += 1
x -= 1
x *= 2
x /= 2
x //= 2
```
...
```
x %= 2
x **= 2
```
---

## Review 

`stack_example.py`

1. What does this do?
2. How can you improve it?

<!-- 2.  Be able to run and understand basic code -->

---

## `bisection.py`

Run it with
```
$ python3 bisection.py
```

Make sure you are in the correct directory!

<!-- 
- Finds the root of a function via the bisection method (range of potential
  roots cut in half at every iteration)
- Take a look at the code, run it, and figure out what everything does (add in
  comments if necessary)
- What happens when you change the tolerance? How can you use different
  functions within the code?
   -->
<!-- 2.  Be able to run and understand basic code -->

---

## Review Data types

<!-- 1. Strings -`'hello world`
2. Numbers - `2.71828` -->

---

## Booleans

`True` or `False` within python

- `True` can also mean non-zero or non-empty or has-length (don't worry too
  much about this now)

- can use `and`, `or`, `not`, and group comparisons logically

- Unlikely to hard code these into the software

<!-- 3. Be able to explain what is and how *control flow* works in python -->
<!-- 5. Learn 10 more Python terms. -->

---

## Comparison Operators

- These operators evaluate to `True` or `False`

1. `==`         `!=` 
1. `>`            `<`
1. `>=`         `<=`

<!-- 3. Be able to explain what is and how *control flow* works in python -->
<!-- 5. Learn 10 more Python terms. -->

---

## Controlling program flow

*pseudo-code*

```python
if condition is True:
    print('true')
elif condition is False:
    print('false')
else:
    print('you will never get here')
```

<!-- quickly walk through. -->

---

## Control Flow Example


  ```python
  x = 5
  if x > 10:
      print('x is large')
  elif x > 2:
      print('x is medium')
  elif x >= 0:
      print('x is small')
  else:  # x < 0
      print('x is negative')
  ```

<!--
- You can nest if statements, and the blocks can be any number of lines long.
- You can call functions within the statements: `if len(l) > 4:`
 -->
<!-- 3. Be able to explain what is and how *control flow* works in python -->
<!-- 5. Learn 10 more Python terms. -->

---

## Data Structures

lists: `l = [1, 2, 3]`

tuples: `t = (1, 2, 3)`

sets: `s = set([1, 2, 3])`

dictionary: `d = {'a': 1, 'b': 2, 'c': 3}`

[https://docs.python.org/3.7/library/stdtypes.html]

<!-- 4. Understand the similarities and differences in the basic python collection types -->
<!-- 5. Learn 10 more Python terms. -->

---

## Reading for next Tuesday

We have a few more basics before we are able to start  writing useful programs.

Think Python: Ch 7, 8.3, and 14.1-.4

*note:* this week we covered Chs. 2, 3 and 5