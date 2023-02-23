# [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
<span style="color:green">Easy</span>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>1996</span></button>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>301</span></button>  Acc: 87.54662189301725
---
Algorithms

Tags:
- Array

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return _a boolean array_ `result` _of length_ `n`_, where_ `result[i]` _is_ `true` _if, after giving the_ `ith` _kid all the_ `extraCandies`_, they will have the **greatest** number of candies among all the kids_ _, or_ `false` _otherwise_.

Note that **multiple** kids can have the **greatest** number of candies.

**Example 1:**


**Input:** candies = [2,3,5,1,3], extraCandies = 3
**Output:** [true,true,true,false,true] 
**Explanation:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

**Example 2:**


**Input:** candies = [4,2,1,1,2], extraCandies = 1
**Output:** [true,false,false,false,false] 
**Explanation:** There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

**Example 3:**


**Input:** candies = [12,1,12], extraCandies = 10
**Output:** [true,false,true]

**Constraints:**

* `n == candies.length`
* `2 <= n <= 100`
* `1 <= candies[i] <= 100`
* `1 <= extraCandies <= 50`

**Hints:**
- Use greedy approach. For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i].

*Generated by [leetcode generator](https://github.com/unsupo/leetcode)*