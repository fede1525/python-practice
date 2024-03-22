from operator import itemgetter

def sort_tuples_ascending(data):

    return sorted(data, key=itemgetter(0, 1, 2))

