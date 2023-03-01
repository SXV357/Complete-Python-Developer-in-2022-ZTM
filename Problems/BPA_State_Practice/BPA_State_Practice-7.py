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

print(LongestPalindrome.longestPalindrome2("cbbd"))