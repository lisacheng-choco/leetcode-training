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