import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.campus_route_finder import bfs_shortest_path


def test_shortest_path():

    graph = {
        "Gate": ["Library", "Canteen"],
        "Library": ["Gate", "Canteen", "Classroom"],
        "Canteen": ["Gate", "Library", "Lab"],
        "Classroom": ["Library", "Lab"],
        "Lab": ["Canteen", "Classroom"]
    }

    path = bfs_shortest_path(
        graph,
        "Gate",
        "Lab"
    )

    assert path is not None
    assert path[0] == "Gate"
    assert path[-1] == "Lab"

    print("Test passed!")
    print("Shortest path:", " -> ".join(path))


if __name__ == "__main__":
    test_shortest_path()
