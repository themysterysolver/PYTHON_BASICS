Here’s the difference between **`del`** and **`remove()`** for both **lists (arrays)** and **dicts**:

---

# **1️⃣ In Lists (Arrays)**

### **`del` → delete by index or slice**

```python
arr = [10, 20, 30, 40]
del arr[1]       # Removes element at index 1
print(arr)       # [10, 30, 40]

del arr[:]       # Deletes all elements
print(arr)       # []
```

---

### **`remove()` → delete by value**

```python
arr = [10, 20, 30, 20]
arr.remove(20)   # Removes **first occurrence** of value 20
print(arr)       # [10, 30, 20]
```

✅ If the value doesn’t exist, `remove()` → **ValueError**
✅ If the index doesn’t exist, `del arr[i]` → **IndexError**

---

# **2️⃣ In Dictionaries**

### **`del` → delete by key**

```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['b']
print(d)         # {'a': 1, 'c': 3}
```

⚠️ If key is missing → **KeyError**

---

### **`.pop()` → delete by key and return value**

```python
d = {'a': 1, 'b': 2, 'c': 3}
val = d.pop('b') 
print(val)       # 2
print(d)         # {'a': 1, 'c': 3}
```

You can also give a default:

```python
d.pop('z', None) # Avoids KeyError
```

---

🔹 **No `remove()` in dicts**, only `del`, `pop()`, or `popitem()`.

---

Would you like me to prepare a **“Python Delete Operations Cheat Sheet”** (covering `del`, `remove()`, `pop()`, `discard()`, `clear()` for lists, dicts, sets) for quick revision before your Glider test?
