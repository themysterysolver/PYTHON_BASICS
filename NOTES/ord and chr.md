Here’s a quick guide for **`ord()`, `chr()`, and rotation logic** in Python:

---

### **1️⃣ ord() and chr() Basics**

* `ord(char)` → Returns the **ASCII (Unicode) value** of a character.
* `chr(number)` → Returns the **character** represented by that ASCII code.

Example:

```python
print(ord('A'))   # 65
print(ord('a'))   # 97

print(chr(65))    # 'A'
print(chr(97))    # 'a'
```

---

### **2️⃣ Rotating a Character by k Positions**

You often need to **shift letters** (like Caesar Cipher).

Example (rotate lowercase letters only):

```python
def rotate_char(ch, k):
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    else:
        return ch
```

---

### **3️⃣ Rotating a Whole String**

```python
text = "abc xyz"
k = 3
rotated = ''.join(rotate_char(c, k) for c in text)
print(rotated)  # "def abc"
```

---

### **4️⃣ Example for Reverse Rotation (Decrypt)**

```python
def rotate_back(ch, k):
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') - k) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') - k) % 26 + ord('A'))
    else:
        return ch
```

---

Would you like me to prepare a **5-question mini set on ord/chr and rotation logic** (increasing difficulty, similar to Glider test questions) for practice?
