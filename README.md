# Campus Route Finder Using BFS

## Problem Statement

Find the shortest route between two campus locations on an unweighted graph using Breadth-First Search (BFS).

## Objectives

1. Represent campus locations as an unweighted graph.
2. Implement the BFS algorithm.
3. Find the shortest route between two campus locations.
4. Display the shortest route and hop count.
5. Demonstrate why BFS gives the fewest-edge path.

## Technologies Used

- Python
- Graph Data Structure
- Breadth-First Search (BFS)

## Graph Representation

The campus locations are represented as vertices and the connecting paths are represented as edges.

Example locations:

- Main Gate
- Library
- Canteen
- Lab
- Hostel

## Methodology

1. Create the campus graph.
2. Select the starting location.
3. Select the destination.
4. Initialize a queue and visited set.
5. Explore the graph level by level using BFS.
6. Store the path from the starting location.
7. Display the shortest route and hop count.

## Implementation

The BFS algorithm is implemented in the file:

`campus_route_finder.py`

## Results

### Input

Start Location: Main Gate

Destination: Hostel

### Output

```text
Shortest Route:
Main Gate -> Canteen -> Lab -> Hostel

Hop Count: 3
