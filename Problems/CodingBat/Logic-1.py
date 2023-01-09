# 1
def double_char(str):
    double_arr = [str[i] * 2 for i in range(len(str))]
    return ''.join(double_arr)

# 2
def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'h' and str[i + 1] == 'i':
            count = count + 1
    return count

# 3
def cat_dog(str):
    count_c = 0
    count_d = 0
    for i in range(len(str)):
        if (str[i:i+3]) == 'cat':
            count_c = count_c + 1
        elif (str[i:i+3]) == 'dog':
            count_d = count_d + 1
    if (count_c == count_d):
        return True
    return False

# 4
def count_code(str):
    count = 0
    for i in range(len(str)):
        if (str[i:i+4]) == 'code':
            count = count + 1
        elif (str[i:i+2]) == 'co' and str[i+2:i+3] != 'd' and str[i+3] == 'e':
            count = count + 1
    return count

# 5
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return True
    elif a.endswith(b):
        return True
    elif b.endswith(a):
        return True
    return False

# 6
def xyz_there(str):
    for i in range(len(str)):
        if str[i] == '.' and str[i+1:i+4] == 'xyz':
            return False
    return True