from collections import deque

# Campus map (unweighted graph)
graph = {
    "Main Gate": ["Library", "Canteen"],
    "Library": ["Main Gate", "Lab"],
    "Canteen": ["Main Gate", "Lab"],
    "Lab": ["Library", "Canteen", "Hostel"],
    "Hostel": ["Lab"]
}

def bfs(start, destination):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == destination:
            break

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)

    # Create shortest path
    path = []
    current = destination

    if current not in parent:
        return None

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


# Input
start = input("Enter starting location: ")
destination = input("Enter destination: ")

# Find route
path = bfs(start, destination)

# Output
if path:
    print("\nShortest Route:")
    print(" -> ".join(path))
    print("Hop Count:", len(path) - 1)
else:
    print("\nNo route found.")
