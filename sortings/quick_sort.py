from turtle import left


data = [50,90,70,20,10,30,40,60,80]

class QuickSort():
    def __init__(self) -> None:
        pass

    def sol1(self, data):
        """
        - time complexity: 
        - space complexity:
        """
        # base case
        if len(data) <=1:
            return data

        left, right, pivot = [], [], data[0]
        for num in data[1:]:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)

        left = self.sol1(left)
        right = self.sol1(right)

        return left + [pivot] + right
    
    def sol2(self, arr, start, end):
        """
        - time complexity:
        - space complexity: O(1)
        """
        if start > end:
            return
        
        pivot_idx = self.partition(arr, start, end)
        self.sol2(arr, start, pivot_idx-1)
        self.sol2(arr, pivot_idx+1, end)

        return arr
    
    def partition(self, arr, start, end):
        pivot = arr[start]
        left_pointer = start + 1
        right_pointer =  end

        while True:
            
            while left_pointer <= right_pointer and arr[left_pointer] <= pivot:
                left_pointer += 1
            
            while  left_pointer <= right_pointer and arr[right_pointer] >= pivot:
                right_pointer -= 1
        
            if left_pointer <= right_pointer:
                arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer] 
            else:
                break

        arr[start], arr[right_pointer] = arr[right_pointer], arr[start]

        return right_pointer





qs = QuickSort()
print("--- 1 ---")
print(qs.sol1(data))
print("--- 2 ---")
print(qs.sol2(data, 0, len(data)-1))