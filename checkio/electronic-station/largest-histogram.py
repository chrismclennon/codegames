# August 12, 2017
# https://py.checkio.org/mission/largest-histogram/


def largest_histogram(histogram: list) -> int:
    if not histogram:
        return None
    max_size = 0
    for outer_index, outer_height in enumerate(histogram):
        width, shortest_height = 0, outer_height
        for inner_index, inner_height in enumerate(histogram[outer_index:],
                                                   start=outer_index):
            width += 1
            shortest_height = min(inner_height, shortest_height)
            current_size = width * shortest_height
            max_size = max(max_size, current_size)
    return max_size


assert largest_histogram([5]) == 5
assert largest_histogram([5, 3]) == 6
assert largest_histogram([1, 1, 4, 1]) == 4
assert largest_histogram([1, 1, 3, 1]) == 4
assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
