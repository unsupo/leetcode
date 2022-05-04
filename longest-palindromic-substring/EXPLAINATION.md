## Dumb
Started with dumb check the middle.  This worked well for the examples, but
if the solution wasn't in the middle then it would fail.

```python
if s == s[::-1]:
    return s
l = len(s)
for i in range(1, l):
    if s[i:l] == s[i:l][::-1]:
        return s[i:l]
    if s[:-i] == s[:-i][::-1]:
        return s[:-i]
    if len(s[i:-i]) > 1 and s[i:-i] == s[i:-i][::-1]:
        return s[i:-i]
return s[0]
```

## Recursion

Then moved onto recursion.  Tried multiple different checks, like dividing in half and other
proportions.  However, only moving 1 left and one right proved to be accuracte.

The issue with this is, it was too slow.  So, I added memoizing.  Unfortunately it was still too 
slow and now i used up too much memory on the heap.

```python
if self.is_palindrone(s):  # .97
    return s
if s in self.memoize:
    return self.memoize[s]
a = self.recurse(s[1:])
b = self.recurse(s[:-1])
longest = a if len(a) > len(b) else b  # sorted([a, b], key=lambda x: len(x), reverse=True)[0]
self.memoize[s] = longest
return longest
```

I made a small improvement by writing my own palindrome function instead of 
inverting the string, but still wasn't enough.

```python
def is_palindrone(self, s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            return False
    return True
```

## Start Small
Next I decided to start small instead of big like i had been doing.

Unfortunately this didn't see any improvement in speed.

```python
if self.is_palindrone(s):  # .97
    return s
palendrone = s[0]
# palendrone length
for i in reversed(range(2, len(s))):  # start at length 2
    for j in range(len(s) - i + 1):
        v = s[j:i + j]
        if self.is_palindrone(v):
            return v
return palendrone
```


## Solution
Now was the time to analyze the results i've seen up to this point.
All the solution were `O(n^3)` because they had to loop over the
whole string, loop over all the substrings, and perform a loop to see 
if it was a palendrome.

Why not avoid the second loop and instead loop over the whole string
and loop until you find the largest palendrome?

That was the next soluiton, hoping to get `O(n^2)`



```python
def _Longest_Palindromic_Substring(self, s):
        # expand from center
        def helper(l, r):
            # if left is in bounds, and r is in bounds
            # and left value equals right value then keep going
            # making a bigger and bigger palendrone
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 # move left over
                r += 1 # move right over
            # return palendrome which is between left and right none inclusive
            return s[l + 1:r]

        res = ""
        # start left to right checking for palindromes
        for i in range(len(s)):
            # get biggest palendrome from this (i) location
            # even palendrome check
            tmp = helper(i, i)
            # if it's bigger than already found then make that the biggest
            if len(tmp) > len(res):
                res = tmp
            # odd palendrome check
            tmp = helper(i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res
```
