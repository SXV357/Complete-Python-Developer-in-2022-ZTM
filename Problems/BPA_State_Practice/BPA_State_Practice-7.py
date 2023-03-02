from collections import Counter
from random import choice
#1
class LongestPalindrome():
    def longestPalindrome1(s: str):
        # Base case(If the given string itself is a palindrome)
        if s == s[::-1]:
            return s
        else:
            chars = list(s)
            res = []
            for i in range(len(chars)):
                current = chars[i]
                res.append(current)
                remaining = chars[i+1:]
                for j in range(len(remaining)):
                    res.append(current + ''.join(remaining[:j+1]))
            modified = list(filter(lambda x: x == x[::-1], res))
            return max(modified, key = lambda val: len(val))    
    
    # Attempt at a more optimized solution with less time complexity
    def longestPalindrome2(s: str):
        # Base case
        if s == s[::-1]:
            return s
        chars = list(s)
        possible_palindromes = []
        for i in range(len(chars)):
            current = chars[i]
            remaining = chars[i+1:]
            isPalindrome = False
            for j in range(len(remaining)):
                combined = current + ''.join(remaining[:j+1])
                if combined == combined[::-1]:
                    possible_palindromes.append(combined)
                    isPalindrome = True
            if isPalindrome:
                break
        # 2 pointers to sift through the array and check for all possible palindromes in a faster way
        for k in range(1, len(chars)):
            lp, rp = k, len(chars) - 1
            while lp < rp:
                if ''.join(chars[lp:rp+1]) == ''.join(chars[lp:rp+1])[::-1]:
                    possible_palindromes.append(''.join(chars[lp:rp+1]))
                    break
                else:
                    rp -= 1
        return max(possible_palindromes, key = lambda val: len(val)) if possible_palindromes else choice(chars)   

#2
def convert(s: str, numRows: int):
    # Base case
    if numRows == 1:
        return s
    if numRows == 2:
        if len(s) > 1:
            first, second = "", ""
            for i in range(0, len(s), 2):
                first += s[i]
            for j in range(1, len(s), 2):
                second += s[j]
            return first + second
        else:
            return s
    if numRows > 2:
        # freq = dict(Counter(list(s)))
        freq = list(s)
        columns = []
        for x in range(0, len(s), (numRows + (numRows - 2))):
            sequence = s[x:x+numRows]
            columns.append(''.join(sequence))
        for val in columns:
            for char in val:
                freq.remove(char)
        if numRows == 3:
           maxLen = max([len(y) for y in columns])
           modifiedFreq = list(filter(lambda i: len(i) < maxLen, columns))[0]
           for _ in range(len(modifiedFreq) + 1, maxLen):
                freqCopy += "*"
           columns.pop()
           columns.append(modifiedFreq)
           return list(zip(*[list(i) for i in columns])) 
        if numRows > 3:
            pass
    
print(convert("PAYPALISHIRING", 3))