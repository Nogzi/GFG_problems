# Minimum Number in a Sorted Rotated Graph

**Difficulty: Easy**

Given an array of distinct elements which was initially sorted. This array is rotated at some unknown point. The task is to find the minimum element in the given sorted and rotated array. 

**Example**:
---

Input:  
N = `10`  
arr[] = `{2, 3, 4, 5, 6, 7, 8, 9, 10, 1}`  
output: `l`  
Explanation: The array is rotated once anti-clockwise. So minimum elemnet is at index (n-1). Which is 1

**Task**
---
The task is to complete the function minNumber() which takes the array arr[] and its starting and ending indices (low and high) as inputs and returns the minimum element in the given sorted and rotated array.

Expected Time Complexity: `O(LogN)`.  
Expected Auxiliary Space: `O(LogN)`.

Constraints:  
`1 <= N <= 10^7`  
`1 <= arr[i] <= 10^7`

[The exercise](https://practice.geeksforgeeks.org/problems/minimum-number-in-a-sorted-rotated-array-1587115620/1)
---
**Thoughts**
---

As per usual it is important to break down the problem as much as possible, before trying to implement the solution. Looking at the initial constraints, the expected time complexity of the solution should be or as close to O(LogN). To achieve this the solution should try to divide the array, until it reaches the base case of the problem.

Taking the example array of `{2, 3, 4, 5, 6, 7, 8, 9, 10, 1}`. we can see that as long as the rotation of the array is anti-clockwise, the smallest number will always be on the right-hand side of the array middle (unless it's the actual middle :) ). We can also see that the middle on a anti-clockwise rotation, will be greater then the length of the array divide by 2.

`{2, 3, 4, 5, 6}` and `{7, 8, 9, 10, 1}`

We can therefore by looking at the middle of the array, decide which side of the array have to search next. From here on out is simple to do this, until there is only one element remainig.

