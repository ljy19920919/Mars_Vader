import doctest
from itertools import permutations


def distance(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def total_distance(points):
    """
    Returns the length of the path passing throught
    all the points in the given order.
    """
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])

def travelling_salesman(points, start):
    """
    Finds the shortest route to visit all the cities by bruteforce.
    Time complexity is O(N!), so never use on long lists.
    """
    points.insert(0, start)
    minimum_path = min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)
    return minimum_path

def faster_travelling_salesman(points, start):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city, but may not have the real minimum path
    """
    points.insert(0, start)
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path


def main():
    doctest.testmod()
    points = [[0, 0], [2, 0]]
    start = [1, 1]
    print("""The minimum distance to visit all the following points: {}
starting at {} is {}.
The faster algoritmh yields a path long {}. """.format(
        tuple(points),
        start,
        total_distance(travelling_salesman(points, start)),
        total_distance(faster_travelling_salesman(points, start))))


if __name__ == "__main__":
    main()
