from operator import itemgetter

def sort_tuples_ascending(data):
    data = [tuple(map(lambda x: x.strip(), item.split(","))) for item in data]
    return sorted(data, key=itemgetter(0, 1, 2))

