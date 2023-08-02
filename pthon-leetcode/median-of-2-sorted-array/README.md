Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

<br>
<br>
1st approach basically fails in the test case:
where num1 = [1,2] ans num2 = [3,4]
Basically at line no 18 'i' goes out of index.

<br>
<br>
efficiency of submitted code: 
<br>
<strong>Runtime Details</strong>
101ms
Beats 77.33%of users with Python3
<br>
<strong>Memory Details</strong>
16.49mb
Beats 95.42%of users with Python3
