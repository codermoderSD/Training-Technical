## String

> - var = "Shubham"
> - var[0] = "S" --> Indexing
> - var[2] = "u" --> Positive Indexing
> - var[-1] = "m" --> Negative Indexing
> - The flow of the indexing is ----> (right to left)

<br>

### Indexing basics

<br>

```
    ------------------------>
    0   1   2   3   4   5   6
    S   H   U   B   H   A   M
   -7  -6  -5  -4  -3  -2  -1
```

```python
var[0:4]
```

Here 0 is the Starting Point and 4 is the Ending point. <br />
The ending point is always n-1. <br />
Thus it will return "SHUB". <br />
This is called positive indexing. <br />

```python
var[-4:-1]
```

Here -4 is the Starting Point and -1 is the Ending point. <br />
The ending point is always n-1. <br />
Thus it will return "BHA". <br />
This is called positive indexing. <br />

- Literals

  - It consists of a value but cannot be declared as a variable.
  - Eg. True is a literal as it consists a value 1 but we cannot use it as a variable name.

- Keywords
  - Any reserved word that gives understanding and does not contain any value is called _keyword_
  - Eg. if, else, for, etc.

<br />

## Conditionals

<br />

### if else

```python
if condition:
    pass        #True block
else:
    pass        #False block
```

- **pass** is a special keyword which just does nothing

<br />

### for loop

```python
for i in range(0,10):
    print(i)
```

This will give digits 0 to 9

```python
name = "Shubham"
for letter in name:
    print(letter)
```

This will loop through individual letter in the string

### while loop

```python
i=0
while i<10:
    print(i)
    i=i+1
```
