class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = []
        num = nums1 + nums2
        num.sort()
        mid = len(num) // 2
        if len(num) % 2 == 0:
            return (num[mid - 1] + num[mid]) / 2.0
        else:
            return num[mid]
