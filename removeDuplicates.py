'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index]== nums[i]
        return unique_index +1


class Solution1:
  def remove_duplicates(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()  # To maintain order since sets do not preserve order
    nums[:len(unique_nums)] = unique_nums  # Modify original array
    return len(unique_nums)



'''If I skip the step that replaces the first part of nums with the sorted unique elements,
the function will still return the count of unique elements, but it will not modify the original list.
The deduplicated and sorted data will be in a separate list (unique_nums), leaving the original list (nums) unchanged.
This approach sacrifices the in-place modification aspect, which may or may not be suitable depending on the problem requirements.'''
