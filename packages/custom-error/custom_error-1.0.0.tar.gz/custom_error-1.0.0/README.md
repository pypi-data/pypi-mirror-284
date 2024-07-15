# Custom Error

Script to throw custom errors in Python

> Create your custom errors and I have control of them with Custom Error

## Use

```python
'''
Test of the module Custome Error
'''
from custom_error import Error

if __name__ == '__main__':
    try:
        number:float = -0.2

        if number < 0.0 or number > 1.0:
            raise Error("Only ranges between 0.0 and 1.0 are allowed", "Invalid Range")
    except Error as e:
        print(e.info())

```

## Sintax

```python
Error(message:str, type_error:str = '')
```

**type_error** (str): Type of the error (optional).<br>
**message** (str): Error message (defaults to an empty string).

```python
Error('My message of error', 'Type of error (optional)')
```

## Show info of error
```python
err = Error('Erro1') #With instance
print(err.info())   #Using method info() -> str

print(Error("Error 2", "Test").info())
```
