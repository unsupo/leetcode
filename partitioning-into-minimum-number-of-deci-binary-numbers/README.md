# [1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)
<span style="color:red">Medium</span>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>1866</span></button>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>1219</span></button>  Acc: 89.75463558796892
---
Algorithms

Tags:
- String
- Greedy

A decimal number is called **deci-binary** if each of its digits is either `0` or `1` without any leading zeros. For example, `101` and `1100` are **deci-binary**, while `112` and `3001` are not.

Given a string `n` that represents a positive decimal integer, return _the **minimum** number of positive **deci-binary** numbers needed so that they sum up to_ `n`_._

**Example 1:**


**Input:** n = "32"
**Output:** 3
**Explanation:** 10 + 11 + 11 = 32

**Example 2:**


**Input:** n = "82734"
**Output:** 8

**Example 3:**


**Input:** n = "27346209830709182346"
**Output:** 9

**Constraints:**

* `1 <= n.length <= 105`
* `n` consists of only digits.
* `n` does not contain any leading zeros and represents a positive integer.

**Hints:**
- Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
- If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
- Thus the answer is equal to the max digit.

*Generated by [leetcode generator](https://github.com/unsupo/leetcode)*