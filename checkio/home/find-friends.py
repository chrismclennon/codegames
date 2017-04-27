# April 28, 2016
# https://checkio.org/mission/find-friends

def check_connection(network, start, goal):
    paths = [start]
    while paths:
        new_paths = []
        for path in paths:
            subject = path.split('-')[-1]
            relatives = [relative for relationship in network if subject in relationship.split('-') for relative in relationship.split('-') if subject not in relative]
            if goal in relatives: 
                return True
            new_paths.extend([path+'-'+relative for relative in relatives if relative not in path.split('-')]) # Check all paths for loops and expand paths
        paths = new_paths
    return False

if __name__ == '__main__':
    network = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")
 
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(network,'scout2','scout3') == True, "Scout Brotherhood"
    assert check_connection(network,'super','scout2') == True, "Super Scout"
    assert check_connection(network,'dr101','sscout') == False, "I don't know any scouts"

