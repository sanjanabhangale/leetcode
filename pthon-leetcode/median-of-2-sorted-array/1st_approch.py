class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        temp = temp1 = 0
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2 != 0:
            while (i+j) != int(((m+n)/2)+1) :
                if nums1[i] >= nums2[j]:
                    temp = nums2[j]
                    j = j+1
                else:
                    temp = nums1[i]
                    i = i+1
            return temp
        else:
            while (i+j) != int(((m+n)/2)+1) and i<m and j<n:
                if nums1[i] >= nums2[j]:
                    temp = temp1
                    temp1 = nums2[j]
                    j = j+1
                else:
                    temp = temp1
                    temp1 = nums1[i]
                    i = i+1
            return (temp + temp1)/2