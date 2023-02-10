import re
#1

# Notes
    # --> (?<=)\&\&(?=) will match all occurrences of && in the string with the replacement
    # --> Searches from start to end and once it finds this pair with spaces on either side, it replaces it

def replace_strings(string):
    pattern1 = "&&"
    pattern2 = "||"
    if len(re.findall(pattern1, string)) >= 1:
        splitted = string.split("&&")
        chars = list(splitted[0])
        if re.search(r"[&&]{2}[&]", string) or chars[-1] != ' ':
            pass
        else:
            string = re.sub("[&&]{2}", "and", string)
    elif len(re.findall(pattern2, string)) >= 1:
        splitted2 = string.split("||")
        chars2 = list(splitted2[0])
        if re.search(r"[||]{2}[|]", string):
            pass
        elif not re.search(r"[||]{2}[|]", string) or chars2[-1] != ' ':
            pass
        else:
            string = re.sub("[||]{2}", "or", string)
    return string

if __name__ == "__main__":
    lines = int(input())
    sentences = []
    for i in range(lines):
        sentence = input()
        sentences.append(sentence)
    res = list(map(replace_strings, sentences))
    for val in res:
        print(val, end = "\n")