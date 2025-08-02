You can get the input in Python like this:

```python
arr = list(map(int, input().split()))
num, x, y = map(int, input().split())
```

But since you want **an array, a number, and 2 integers separated by 2 spaces**, you can do it step by step:

```python
# Input example:
# 1 2 3 4 5
# 10 20 30

arr = list(map(int, input().split()))   # First line: array
num, a, b = map(int, input().split())   # Second line: number and 2 integers

print(arr)
print(num, a, b)
```

### Example Input:

```
1 2 3 4 5
10 20 30
```

### Output:

```
[1, 2, 3, 4, 5]
10 20 30
```

Would you like me to give you a **list of 10 quick practice problems** on these three topics (logic, arrays/linked lists, strings) that are commonly asked on Glider tests?
