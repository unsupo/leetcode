*%s*
</br>%s %s %s
</br>---
</br>%solution](/problems/two-sum/solution/)[Discuss](/problems/two-sum/discuss/)[Submissions](/problems/two-sum/submissions/)1. Two SumEasy317531004Add to ListShareGiven an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.


You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.


You can return the answer in any order.


 


**Example 1:**



```
**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**



```
**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

```

**Example 3:**



```
**Input:** nums = [3,3], target = 6
**Output:** [0,1]

```

 


**Constraints:**


* `2 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* **Only one valid answer exists.**


 


**Follow-up:**Can you come up with an algorithm that is less than `O(n2)`time complexity?Accepted6.5MSubmissions13.4MCompaniesRelated Topics[Array](/tag/array/)[Hash Table](/tag/hash-table/)Similar Questions[3Sum](/problems/3sum/)Medium[4Sum](/problems/4sum/)Medium[Two Sum II - Input Array Is Sorted](/problems/two-sum-ii-input-array-is-sorted/)Medium[Two Sum III - Data structure design](/problems/two-sum-iii-data-structure-design/)Easy[Subarray Sum Equals K](/problems/subarray-sum-equals-k/)Medium[Two Sum IV - Input is a BST](/problems/two-sum-iv-input-is-a-bst/)Easy[Two Sum Less Than K](/problems/two-sum-less-than-k/)Easy[Max Number of K-Sum Pairs](/problems/max-number-of-k-sum-pairs/)Medium[Count Good Meals](/problems/count-good-meals/)Medium[Count Number of Pairs With Absolute Difference K](/problems/count-number-of-pairs-with-absolute-difference-k/)Easy[Number of Pairs of Strings With Concatenation Equal to Target](/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/)Medium[Find All K-Distant Indices in an Array](/problems/find-all-k-distant-indices-in-an-array/)EasyShow Hint 1A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.Show Hint 2So, if we fix one of the numbers, say 
```
x
```
, we have to scan the entire array to find the next number 
```
y
```
 which is 
```
value - x
```
 where value is the input parameter. Can we change our array somehow so that this search becomes faster?Show Hint 3The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?#### Sign in to view your submissions.

Sign in 