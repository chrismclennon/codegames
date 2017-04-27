def checkio(data):
    try:
        return data[0] + checkio(data[1:])
    except IndexError:
        return data[0]
