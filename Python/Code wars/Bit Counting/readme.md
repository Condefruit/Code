You can find the exercice <a href="https://www.codewars.com/kata/526571aae218b8ee490006f4" target="_blank"> here </a>

The mission statement :
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

My answer :
```Python
def count_bits(n):
    c = str("{0:b}".format(n))
    a = 0
    for i in range(len(c)) :
        if int(c[i]) == 1 :
            a+=1
    return(a)
```

Smart choice could also be :
```Python
def countBits(n):
    return bin(n).count("1")
```
using the native function bin(x) and the count() method.

