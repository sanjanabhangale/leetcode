class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        temp = temp1 = 0
        m = len(nums1)
        n = len(nums2)
        def getvalue(k):
            i = j = 0
            while i<m and j<n and (i+j) != k:
                if nums1[i] >= nums2[j]:
                    temp = nums2[j]
                    j = j+1
                else: 
                    temp = nums1[i]
                    i = i+1
            while i<m and (i+j) != k:
                temp = nums1[i]
                i = i+1
            while j<n and (i+j) != k:
                temp = nums2[j]
                j = j+1
            return temp


        if (m+n)%2 != 0:
            temp = getvalue(((m+n)//2)+1)
            return temp
        else:
            temp = getvalue(((m+n)//2)+1)
            temp1 = getvalue(((m+n)//2))
            return (temp + temp1)/2




"""
Accepted

Runtime
Details
101ms
Beats 77.33%of users with Python3

Memory
Details
16.49mb
Beats 95.42%of users with Python3

"""