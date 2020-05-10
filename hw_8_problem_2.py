"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    len_ = 1
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)): # Access passed in array which could be n elements long so O(n) time.
        if nums[i] != nums[i-1]:
            nums[len_] = nums[i]
            len_ +=1
    return len_

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

# Overall the time complexity looks to be O(n) time.