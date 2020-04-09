class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for num, num_1 in enumerate(nums):
            remaining = target - num_1
            if remaining in visited:
                return [visited[remaining], num]
            visited[num_1] = num
        return None
        
