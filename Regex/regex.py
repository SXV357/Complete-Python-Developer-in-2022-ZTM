import re

newStr = 'This is a random string to search a term in'
# searching for the string "random":
# conventional --> "random" in newStr
# with regex
# string to search for, main string(returns Match object)
print(re.search("random", newStr))

a = re.search("term", newStr)
# starting + ending index where target string occurs returned as a tuple
print(a.span())
print(a.start())  # staring index
print(a.end())  # ending index
print(a.group())  # string that matched

primaryPattern = re.compile("random")
c = primaryPattern.search(newStr)
# all instances of compiled term in newStr
print(primaryPattern.findall(newStr))
# .fullMatch() only works if what we're searching for is the exact same as the string itself

# using patterns
anotherString = "Hello. What's good yo? We chill or nah?"
# all letters in range of a-z or A-Z followed by lower case a
compilation = re.compile(r"([a-zA-Z].[a])")
print(compilation.search(anotherString))
print(compilation.search(anotherString).group(1))

# password checker(>= 8, any letters, numbers, but for special chars --> $%#@)

passwordFormat = re.compile(
    r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$%]).{8,}([0-9])")
passwords = ["sIqz@?!91468Ad4", "76uwdhsc$#%$6",
             "%$#JVFGtv&868", "6764GJvr$%$1"]
for i in range(len(passwords)):
    res = passwordFormat.fullmatch(passwords[i])
    print(res)


newPwFormat = re.compile(r"[A-Za-z0-9@#$%]{8,}[0-9]")
newPassword = "TRVnhjv5$%$89"
print(newPwFormat.search(newPassword))
