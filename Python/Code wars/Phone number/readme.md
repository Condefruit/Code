You can find the exercice <a href="https://www.codewars.com/kata/525f50e3b73515a6db000b83" target="_blank"> here </a>

The mission statement :
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

My answer :
```Python
def create_phone_number(n):
    return ('('+str(n[0])+str(n[1])+str(n[2])+')'+' '+str(n[3])+str(n[4])+str(n[5])
            +'-'+str(n[6])+str(n[7])+str(n[8])+str(n[9]))
```

Smart choice could also be :
```Python
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
```
using placeholders (defined by {}), the format function and the * operator (which is known, in this context, as the tuple (or iterable) unpacking operator).

