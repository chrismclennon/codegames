# July 27, 2016
# https://checkio.org/mission/restricted-sum/

def checkio(data):
    try:
        return data[0] + checkio(data[1:])
    except IndexError:
        return data[0]
