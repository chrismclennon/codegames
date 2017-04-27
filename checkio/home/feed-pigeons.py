# April 29, 2016
# https://checkio.org/mission/feed-pigeons/

def checkio(portions):
    pigeons = list()
    fly_by = 1

    while portions > 0:
        pigeons.extend([0] * fly_by)
        fly_by += 1
        
        i = 0
        while portions > 0 and i < len(pigeons):
            pigeons[i] += 1
            portions -= 1
            i += 1
   
    return len([x for x in pigeons if x > 0])    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
