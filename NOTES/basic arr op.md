Here’s a **quick reference for Python list operations** (most commonly used in coding tests like Glider):

---

## **1️⃣ Creating a List**

```python
arr = [1, 2, 3]
empty_list = []
mixed = [1, "a", True]
```

---

## **2️⃣ Adding Elements**

```python
arr.append(4)        # [1, 2, 3, 4]
arr.insert(1, 10)    # [1, 10, 2, 3, 4]
arr.extend([5, 6])   # [1, 10, 2, 3, 4, 5, 6]
```

---

## **3️⃣ Removing Elements**

```python
arr.pop()            # Removes last element
arr.pop(1)           # Removes element at index 1
arr.remove(3)        # Removes first occurrence of 3
arr.clear()          # Removes all elements
```

---

## **4️⃣ Accessing Elements**

```python
arr = [10, 20, 30, 40]
print(arr[0])        # 10
print(arr[-1])       # 40
print(arr[1:3])      # [20, 30]
```

---

## **5️⃣ Searching & Counting**

```python
arr.index(30)        # 2 (first occurrence)
arr.count(20)        # Counts occurrences
```

---

## **6️⃣ Sorting and Reversing**

```python
arr.sort()           # Sort in ascending order
arr.sort(reverse=True)  # Descending
arr.reverse()        # Reverse list order
```

---

## **7️⃣ Copying Lists**

```python
copy_arr = arr.copy()    # Shallow copy
```

---

## **8️⃣ Combining Lists**

```python
a = [1, 2]
b = [3, 4]
c = a + b               # [1, 2, 3, 4]
```

---

## **9️⃣ Checking Membership**

```python
print(2 in arr)          # True
print(100 not in arr)    # True
```

---

## **🔟 Other Useful Operations**

```python
len(arr)                 # Number of elements
sum(arr)                 # Sum of elements
min(arr)                 # Smallest element
max(arr)                 # Largest element

# List comprehension
squares = [x*x for x in arr]
```

---

Would you like me to make a **"Python Glider Test Rapid-Revision Sheet"** that covers:

* Input tricks
* String ops
* List ops
* `heapq`, `Counter`, `defaultdict`
* `ord()`, `chr()`, rotation logic
  all in **one single page**?
