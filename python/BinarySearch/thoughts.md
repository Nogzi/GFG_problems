# Binary Search

**Difficulty: Basic**

Given a sorted array of size **N** and an integer **K**, find the position at which **K** is present in the array using binary search.

**Example**
---
Input:  
N = `5`  
arr[] = `{1 2 3 4 5}`  
K = `4`  
Output: 3  
Explanation: 4 appears at index 3.

**Task**
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.

Expected Time Complexity: O(LogN)  
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.  

**Thoughts**
---
To perform a binary search on the array, we have to start by splitting the array and identify on which side of the array we have to continue on. Given that the list given to us is sorted by default, we can simply deside this based on if the middle of the array is greater or smaller then `K`.

In the above example, the array would be spilt `{1 2}` and `{3 4 5}` after the first interation of a recursive version of our binary search. 
