# 10. Regular Expression Matching
<span style="color:red">Hard</span>. :thumbsup:8029 :thumbsdown:1215<br/>

---
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:


* `'.'` Matches any single character.​​​​
* `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).


 



<br/>****Example 1:****


<pre>
<b>Input:</b> s = "aa", p = "a"
<b>Output:</b> false
<b>Explanation:</b> "a" does not match the entire string "aa".
</pre>
****Example 2:****


<pre>
<b>Input:</b> s = "aa", p = "a\*"
<b>Output:</b> true
<b>Explanation:</b> '\*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>
****Example 3:****


<pre>
<b>Input:</b> s = "ab", p = ".\*"
<b>Output:</b> true
<b>Explanation:</b> ".\*" means "zero or more (\*) of any character (.)".
</pre>

**Constraints:**


* `1 <= s.length <= 20`
* `1 <= p.length <= 30`
* `s` contains only lowercase English letters.
* `p` contains only lowercase English letters, `'.'`, and `'*'`.
* It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.



