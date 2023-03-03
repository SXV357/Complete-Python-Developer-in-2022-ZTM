from collections import Counter
from itertools import groupby
import math
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
class ZigZagConversion():
    def convert1(s: str, numRows: int):
        # Original Non-Working Approach
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
    
    # Modified approach using matrix traversal
    def convert2(s:str, numRows: int):
        # Base cases
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
        elif numRows > 2:
            s.replace(",", "").replace(".", "")
            maxElemsPerSection = (2 * numRows) - 2 # Elems going down a row and a few going up the diagonal(Since there's numRows - 1 columns in each secction, this is the total number of elements that can be within that)
            totalCols = math.ceil(len(s) / maxElemsPerSection) + numRows
            matrix = [[''] * totalCols for _ in range(numRows)] # Initializing empty matrix
            startIndex, currentRow, currentCol = 0, 0, 0
            # The idea is to keep looping until we exhaust all the characters in the string
            while startIndex < len(s):
            # First while loop to add elements in column major order(Current column stays the same but the row keeps changing by 1 each time)
                while currentRow < numRows and startIndex < len(s):
                    matrix[currentRow][currentCol] = s[startIndex]
                    startIndex += 1
                    currentRow += 1 

                currentRow -= 2 # after adding the first elem, there's such (NumRows - 1) elements that are left to be added so currentRow should technically then start at one less than where we stopped
                currentCol += 1 # Diagonal fashsion so c(next) = prevC + 1(we are traversing from bottom left to top right for n iterations)

            # Second while loop to add elements in a diagonal fashion from left to right
            # For numRows = 4, there's exactly two elements in between each column so since we're already starting at row 2 we are going until 0 each time
                while currentRow > 0 and currentCol < totalCols and startIndex < len(s):
                    matrix[currentRow][currentCol] = s[startIndex]
                    currentRow -= 1 # Rows decrease on each iteration
                    currentCol += 1 # Columns increase on each iteration
                    startIndex += 1

            # Logic to traverse the matrix in row major order and print all letters line-by-line
            res = ""
            for row in matrix:
                for val in row:
                    res += val
            res.replace(" ", "")
            return res

#3
def compress(chars: list[str]):

    # # 2-pointer approach
    # res = []
    # lp, rp = 0, len(chars) - 1
    # while lp < rp:
    #     arr = chars[lp:rp+1]
    #     counter = 0
    #     for i in range(len(arr) - 1):
    #         if arr[i] == arr[i+1]:
    #             counter += 1
    #     if counter == len(arr) - 1:
    #         res.append(arr)
    #         lp += 1
    #         break
    #     if counter < len(arr):
    #         rp -= 1
    # return res

    # freq = [[val, chars.count(val)] for val in chars]
    # freq = sorted([list(x) for x in list(set(tuple(x) for x in freq))])
    # s = ""
    # for combination in freq:
    #     if combination[1] == 1:
    #         s += combination[0]
    #     if combination[1] > 1:
    #         s += combination[0] + str(combination[1])
    # chars[:] = list(s)

    string_rep = ''.join(chars)
    res = []
    for char, collection in groupby(string_rep):
        res.append([char, len(list(collection))])
    s = ""
    for combination in res:
        if combination[1] == 1:
            s += combination[0]
        if combination[1] > 1:
            s += combination[0] + str(combination[1])
    chars[:] = list(s)
    return s

print(compress(["a","a","a","b","b","a","a"]))
