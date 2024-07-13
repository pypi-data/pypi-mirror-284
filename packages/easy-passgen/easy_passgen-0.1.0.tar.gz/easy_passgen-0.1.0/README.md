# Easy Password Generator

Tool for generating random passwords. You can choose if you want just letters or letters and special characters.

## Installation

You can install the package using `pip3`:

```python
pip3 install easy_passgen
```

## Use

```python
from easy_passgen import Generator

# Create an instance of the Generator
gen = Generator(12, True) # 12 is the length of the password, and True indicates that you want special characters

# Generate password
password = gen.generate()

#Generate and print password
gen.generate_and_print()
```
