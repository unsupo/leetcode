# [1773. Count Items Matching a Rule](https://leetcode.com/problems/count-items-matching-a-rule/)
<span style="color:green">Easy</span>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>1187</span></button>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>128</span></button>  Acc: 84.26761569568151
---
Algorithms

Tags:
- Array
- String

You are given an array `items`, where each `items[i] = [typei, colori, namei]` describes the type, color, and name of the `ith` item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The `ith` item is said to match the rule if **one** of the following is true:

* `ruleKey == "type"` and `ruleValue == typei`.
* `ruleKey == "color"` and `ruleValue == colori`.
* `ruleKey == "name"` and `ruleValue == namei`.

Return _the number of items that match the given rule_.

**Example 1:**


**Input:** items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
**Output:** 1
**Explanation:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].

**Example 2:**


**Input:** items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
**Output:** 2
**Explanation:** There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

**Constraints:**

* `1 <= items.length <= 104`
* `1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10`
* `ruleKey` is equal to either `"type"`, `"color"`, or `"name"`.
* All strings consist only of lowercase letters.

**Hints:**
- Iterate on each item, and check if each one matches the rule according to the statement.

*Generated by [leetcode generator](https://github.com/unsupo/leetcode)*