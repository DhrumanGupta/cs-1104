from itertools import combinations

S = {1, 2, 3}
SxS = [(x, y) for x in S for y in S]


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def is_square(points):
    distances = sorted(
        distance(points[i], points[j]) for i in range(4) for j in range(i + 1, 4)
    )
    # There should only be 2 unique distances: the diagonal and the side
    # We sort the distances. So the lowest distance (the side length) should be a total of 4.
    return len(set(distances)) == 2 and distances.count(distances[0]) == 4


squares = list(set([comb for comb in combinations(SxS, 4) if is_square(comb)]))
print(len(squares))
print(squares)
