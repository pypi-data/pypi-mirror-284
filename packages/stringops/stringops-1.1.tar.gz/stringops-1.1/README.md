# Overview

Complex lines of code for manipulating strings are no more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Installation is pretty easy.

```sh
pip install stringops
```

## Usage

### Manipulation

> Import the necessary extended class

```python
from stringops.manipulation import Manipulation
```

> Manipulate -> add

```python
# suppose there is some string say 'value'

value = "Hey This is me"

# I want to add a '.' at the end

value = Manipulation(value)
value = value.add(".")

# I also want to add another sentence to it.

value = value.add("How are you", "!")

# print it
print(value)
```

> Manipulate -> half

```python
# lets take the above variable 'value'.

value = Manipulation("hey, this is me")

# I want to divide the string into half and i want to get the left side of the result.

left_half = value.half("left")
right_half = value.half("right")

print(left_half, right_half)
```

> Manipulate -> split

```python
# using the same varibale 'value'.

value = Manipulation("hey, this is me")

# suppose i want to split the string based on white spaces and
# get the value that is in the index place of 1

# can be done using
# >>> value.split(" ")[1]

index_one_value: str = value.split(" ", 1)

# all the values can also be retrieved
all_values: list[str] = value.split(" ", "all")
```

> CONVERT THIS `MANIPULATION` OBJECT TO `READ`

```python
value: Manipulation = Manipulation("hey, this is me")
value: Read = value.convert_to_read()
```

### Read

> Importing

```python
from stringops.read import Read
```

> Read - check substring

```python
value = Read("hey, this is me")

if value.there("he"):
    return True
else:
    return False
```