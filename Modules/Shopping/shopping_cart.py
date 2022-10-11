print(__name__)
def buy_something(item):
    res = []
    for i in range(0, item + 1):
        res.append(i)
    return res