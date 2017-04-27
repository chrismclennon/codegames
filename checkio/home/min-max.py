# May 4, 2016
# https://checkio.org/mission/min-max/

def min(*args, **kwargs):
    key = kwargs.get("key", lambda e: e) 
    if len(args) == 1: 
        args = list(args[0])
    result = args[0]
    for x in range(1,len(args)):
        if key(result) > key(args[x]): 
            result = args[x]
    return result

def max(*args, **kwargs):
    key = kwargs.get("key", lambda e: e)
    if len(args) == 1: 
        args = list(args[0])
    result = args[0]
    for x in range(1,len(args)):
        if key(result) < key(args[x]): 
            result = args[x]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(3, 2) == 2, "Simple case min"
    assert min("hello") == "e", "From string"
    assert min([3,5]) == 3, "Simple case iterator min"
    assert min([1,2],[0,1]) == [0,1], "Comparing two lists"
    assert min([0,1],[1,2],[3,4],[5,6],[7,8]), "Comparing many lists"
    assert min([[1, 2], [3, 4], [9, 0]]) == [1, 2], "list of lists"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

    assert max(3, 2) == 3, "Simple case max"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"

