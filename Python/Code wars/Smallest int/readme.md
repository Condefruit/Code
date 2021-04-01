You can find the exercice <a href="https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python"> here </a>

The mission statement :
Given an array of integers your solution should find the smallest integer.

My answer :
```Python
def find_smallest_int(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    print(arr)
    return arr[0]
```
Bit of overkill but also wanted to sort the array :)

The easier and fastest way would be (straight to the point) :

```Python
def findSmallestInt(arr):
    return min(arr)
```
