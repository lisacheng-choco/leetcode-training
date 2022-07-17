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

### Keywords
- bucket sort: index=count/frequency, value=the elements you want => O(n) => 當需要用dictionary value做排序時