class Friends:
    def __init__(self, connections):
        self._connections = list(connections)

    def add(self, connection):
        if connection in self._connections:
            return False
        self._connections.append(connection)
        return True

    def remove(self, connection):
        if connection not in self._connections:
            return False
        self._connections.remove(connection)
        return True

    def names(self):
        output = set()
        for conn in self._connections:
            output = output.union(set(conn))
        return output

    def connected(self, name):
        output = set()
        for conn in self._connections:
            if name in conn:
                output = output.union(conn)
        if output:
            output.remove(name)
        return output

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

