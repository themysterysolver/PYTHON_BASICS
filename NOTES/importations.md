Both **`heapq`** and **`Counter`** are part of Python's **standard library**:

---

### **1️⃣ `heapq`**

* **Location:** `heapq` module (built-in, no installation needed)
* **Use:** Provides **min-heap priority queue** functions.

Example:

```python
import heapq

nums = [5, 2, 9, 1]
heapq.heapify(nums)      # Convert list to heap
print(nums)              # [1, 2, 9, 5] (heap order)

heapq.heappush(nums, 0)  # Push new element
print(nums)              # [0, 1, 9, 5, 2]

print(heapq.heappop(nums))  # 0 (smallest element)
```

---

### **2️⃣ `Counter`**

* **Location:** `collections` module
* **Use:** Counts occurrences of elements in an iterable.

Example:

```python
from collections import Counter

text = "mississippi"
count = Counter(text)
print(count)           # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(count.most_common(2))  # [('i', 4), ('s', 4)]
```

---

✅ Both modules are **built-in**, you just `import` them; no extra installation is required.

---

Would you like me to make a **cheat sheet of the top 10 built-in Python modules** (like `heapq`, `Counter`, `math`, etc.) that often appear in coding tests?

