# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    segments.sort(key=lambda a: a[1])
    points = [segments[0].end]

    for s in segments:
        if s.start <= points[-1] <= s.end:
            continue
        else:
            points.append(s.end)

    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")
