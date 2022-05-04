# 8. String to Integer (atoi)
<span style="color:yellow">Medium</span>. :thumbsup:1636 :thumbsdown:4772<br/>

---
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).


The algorithm for `myAtoi(string s)` is as follows:


1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-231` should be clamped to `-231`, and integers greater than `231 - 1` should be clamped to `231 - 1`.
6. Return the integer as the final result.

**Note:**


* Only the space character `' '` is considered a whitespace character.
* **Do not ignore** any characters other than the leading whitespace or the rest of the string after the digits.

 



<br/>****Example 1:****


<pre>
<b>Input:</b> s = "42"
<b>Output:</b> 42
<b>Explanation:</b> The underlined characters are what is read in, the caret is the current reader position.
</pre>
****Example 2:****


<pre>
<b>Input:</b> s = "   -42"
<b>Output:</b> -42
<b>Explanation:</b> **Explanation:**
</pre>
****Example 3:****


<pre>
<b>Input:</b> s = "4193 with words"
<b>Output:</b> 4193
<b>Explanation:</b> **Explanation:**
</pre>

**Constraints:**


* `0 <= s.length <= 200`
* `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.



