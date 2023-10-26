

def binarySearch(nums:list,target:int) -> int:
    min_index = 0
    max_index = len(nums) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] < target:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1

result = binarySearch([4,9,15,21,34,57,68,91],68)
print(result)