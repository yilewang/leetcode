class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while right >= left:
            index = left + (right-left)//2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = index+1
            else:
                right = index-1
        else:
            return -1

print(Solution.search(Solution, [-1,0,3,5,9,12], 9))