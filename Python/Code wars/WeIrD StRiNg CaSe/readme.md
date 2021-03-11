You can find the exercice <a href="https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python"> here </a>

The mission statement :
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The zero-ith index is even.

My answer :
```Python
def to_weird_case(string):
    text = ""
    j = 0
    for i in range(len(string)) :
        if j%2 == 0 :
            text = text + string[i].upper()  
        else :
            text = text + string[i].lower() 
        if string[i] != " " :
            j += 1
        else :
            j = 0
    return(text)
```
Smart choice could also be :

```Python
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
```
or

```Python
def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])
```

which are both similar and split the "string" into words and deal with the upper lower case using the string.join function.
