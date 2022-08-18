# leetcode-training


## Notes
### HashTable v.s. HashSet
- HashTable: to record the the occurence in list
- HashSet: to check if the element is duplicated in list

### Iterate list
```python
nums = [2, 3, 11, 7]
for i in range(len(nums)):
    idx = i
    element = nums[i]

for i, num in enumerate(nums):
    idx = i
    element = num
```

### Iterate dictionary's key & value
```python
dic = {"key1": "value1"}

# dic.items() is to make dictionry into list of tuples: List[tuple]
for key, val in dic.items(): 
    key = "key1"
    val = "value1"
```

### dictionary fetch value
如果key不在，新增一組key, value(default=set()) pair , 反之add randmon number to set
```python
num = random num
# 1
dic = {}
if "k" not in dic:
    dic["k"] = set()
else:
    dic[k] = dic[k].add(num)
# 2
dic = collections.defaultdict(set) # 宣告一個dictionary其default value是set()
dic["k"].add(num)

```
----
```python
val = dic.get("key", set()) # if dic 的key不包含"key"，val回傳set()
```

### Reverse a list, string, tuple in Python (reverse, reversed)
- for a list: 
    - l.reverse() (return None)  
    - reversed(l) (return list) 
    - l[::-1]
- for a string or tuple: 
    - reversed(s), reversed(t)
    - s[::-1], t[::-1]

### Determine if a character is aplha or numeric
- use ASCII 
- use Python build-in function: isalnum() / isalpha(), isnumeric()

### Sort by key
```python
# scenario 1: sort list of numbers
a = [1, 5, 3, 4, 2]

a.sort()
heapq.heapify(a)

# scenario 2: sort list of tuples
a = [(1, 0), (5, 1), (3, 2), (4, 3), (2, 4)]

a.sort(key=lambda tup: tup[0]) # sort by the first element of tuple
a.sort(key=lambda tup: tup[1]) # sort by the second element of tuple

heapq.heapify(a) # sort by the by the first element of tuple. if the first elements are equal, then compare the second element

# scenario 2: sort list of lists
a = [[1, 0], [5, 1], [3, 2], [4, 3], [2, 4]]

a.sort(key=lambda lst: lst[0]) # sort by the first element of tuple
a.sort(key=lambda lst: lst[1]) # sort by the second element of tuple

heapq.heapify(a) # sort by the by the first element of tuple. if the first elements are equal, then compare the second element
```

### Keywords
- bucket sort: index=count/frequency, value=the elements you want => O(n) => 當需要用dictionary value做排序時