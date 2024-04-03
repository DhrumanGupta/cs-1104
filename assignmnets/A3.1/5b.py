from itertools import combinations

S = {1, 2, 3}
SxS = [(x, y) for x in S for y in S]


def area_of_triangle(p1, p2, p3):
    return (
        abs(
            p1[0] * p2[1]
            + p2[0] * p3[1]
            + p3[0] * p1[1]
            - p1[1] * p2[0]
            - p2[1] * p3[0]
            - p3[1] * p1[0]
        )
        / 2
    )


triangles = list(
    set([comb for comb in combinations(SxS, 3) if area_of_triangle(*comb) > 0])
)
print(triangles)
print(len(triangles))
