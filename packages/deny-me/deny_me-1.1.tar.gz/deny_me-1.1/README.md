[![Implementation Test](https://github.com/d33pster/deny-me/actions/workflows/Tests.yml/badge.svg)](https://github.com/d33pster/deny-me/actions/workflows/Tests.yml)
[![CD](https://github.com/d33pster/deny-me/actions/workflows/Deploy.yml/badge.svg)](https://github.com/d33pster/deny-me/actions/workflows/Deploy.yml)

# Overview

You must have often wondered about how to make a function restricted to the user so that it could only be called a specific number of time, or even a function that is password protected.

This library provides an array of function decorators that can be used for the same.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Easily restrict any function according to your needs.
- improve overall acessibility of your program.

## Installation

> Install using pip.

```sh
pip install deny-me
```

## Usage

- **Once/Twice**

To make your function run only once.

> import the decorators.

```python
from deny_me.restrict import once, twice
```

> use acording to your needs.

```python
# demo function
# This function will be callable only once.
# Repeated calling will generate error.
class some_class:
    def __init__(self):
        ...

    @once
    def function1(self, name: str, school: str = "ABC"):
        print(f"{name} goes to {school}!")
        ...

    # demo funtion 2
    # This function will be callable two times.
    # will generate error if called more than twice
    @twice
    def function2(self, *args, **kwargs):
        ...
```

> **Note to the users.**

If other decorators are used for a function other than these, then it is recommended to use these decorators at the last.

`For example:`

```python
# demo class
class Demo:
    def __init__(self):
        ...
    
    # suppose you need to define a property
    # that is only callable once.
    @property
    # use property first
    @once
    # and then use once
    def property1(self):
        return ...
    
    # similarly if you want to define a setter
    # for the property.
    @property1.setter # use this
    # and then the once decorator
    @once
    def property1(self, value: str):
        self.value = value
        ...
```

- **Run custom times**

To run a function n times.

> import the Allow class.

```python
from deny_me.restrict import Allow
```

> run n=10 times

```python
# demo function
# this function will run 10 times

class Demo:
    def __init__(Self):
        ...
    
    @Allow(10).times
    def function(self, *args, **kwargs):
        ...
```

> Note: Similar to the Once/Twice decorators, If other decorators are needed, such as `property`, then it should be at the top and the `Allow(n).times` should be the last decorator.

- **Password Protection**

To make your function password protected.

> import the Password class.

```python
from deny_me.password import Password
```

> Use the password decorator.

```python
# demo function
# this function will be password protected.
class some_class:
    def __init__(self):
        ...

    @Password("pass123").protected
    def function(*args, **kwargs):
        ...

    # It is recommended that the above function has `*args` 
    # and `**kwargs` in its parameters.
    # If some parameters are mandatory, they can be defined before 
    # mentioning `*args` and `**kwargs`.
    ## FOR EXAMPLE:

    @Password("pass123").protected
    def function(name: str, school: str = "ABC", *args, **kwargs):
        ... 
```

> **How to call the function?**

```python
# To call the function, just add `password=` parameter 
# while calling.

c = some_class()
c.function(name="hehe", password="pass123")

# This will run fine as the password is correct!
# However, if the password is wrong, it will
# prompt about the same.

# NOTE: if the `password=` parameter is missing while calling
# the function then it will raise an error stating that
# an exclusive feature has been called that is not made
# available to the users.
```