# [2325. Decode the Message](https://leetcode.com/problems/decode-the-message/)
<span style="color:green">Easy</span>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>368</span></button>   <button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>47</span></button>  Acc: 84.64684599653924
---
Algorithms

Tags:
- Hash Table
- String

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

1. Use the **first** appearance of all 26 lowercase English letters in `key` as the **order** of the substitution table.
2. Align the substitution table with the regular English alphabet.
3. Each letter in `message` is then **substituted** using the table.
4. Spaces `' '` are transformed to themselves.
* For example, given `key = "**hap**p**y** **bo**y"` (actual key would have **at least one** instance of each letter in the alphabet), we have the partial substitution table of (`'h' -> 'a'`, `'a' -> 'b'`, `'p' -> 'c'`, `'y' -> 'd'`, `'b' -> 'e'`, `'o' -> 'f'`).

Return _the decoded message_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/05/08/ex1new4.jpg) 


**Input:** key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
**Output:** "this is a secret"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "**the** **quick** **brown** **f**o**x** **j**u**mps** o**v**er the **lazy** **d**o**g**".

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/05/08/ex2new.jpg) 


**Input:** key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
**Output:** "the five boxing wizards jump quickly"
**Explanation:** The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "**eljuxhpwnyrdgtqkviszcfmabo**".

**Constraints:**

* `26 <= key.length <= 2000`
* `key` consists of lowercase English letters and `' '`.
* `key` contains every letter in the English alphabet (`'a'` to `'z'`) **at least once**.
* `1 <= message.length <= 2000`
* `message` consists of lowercase English letters and `' '`.

**Hints:**
- Iterate through the characters in the key to construct a mapping to the English alphabet.
- Make sure to check that the current character is not already in the mapping (only the first appearance is considered).
- Map the characters in the message according to the constructed mapping.

*Generated by [leetcode generator](https://github.com/unsupo/leetcode)*