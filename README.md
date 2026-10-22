# Campus Route Finder Using Breadth-First Search (BFS)

## Project Overview

The Campus Route Finder is a graph-based application that finds the shortest route between two locations on a campus using Breadth-First Search (BFS).

Each campus location is represented as a vertex and each direct connection is represented as an edge. Since the campus graph is unweighted, BFS explores locations level by level and finds a path with the minimum number of edges.

## Problem Statement

Students and visitors may find it difficult to determine the shortest route between two locations on a large campus.

This project provides a simple solution by representing campus locations as a graph and using BFS to find the shortest route between a starting location and a destination.

## Objectives

- Represent campus locations using a graph.
- Implement Breadth-First Search (BFS).
- Find the shortest route between two locations.
- Display the shortest path clearly.
- Calculate the hop count.
- Demonstrate why BFS gives the fewest-edge path.

## Technologies Used

- Python
- Graph Data Structure
- Breadth-First Search
- Queue
- GitHub

## Methodology

### Step 1: Create Graph

Campus locations are represented as vertices and connecting routes are represented as edges.

### Step 2: Initialize BFS

The selected starting location is added to the queue.

### Step 3: Explore Neighbors

BFS visits connected locations level by level.

### Step 4: Track Parent

The previous location of each visited location is stored.

### Step 5: Find Destination

The algorithm continues until the destination is reached.

### Step 6: Reconstruct Path

The parent information is followed backwards to obtain the complete route.

## Why BFS Finds the Shortest Path

BFS explores an unweighted graph level by level.

```text
Level 0 → Starting location
Level 1 → Locations 1 hop away
Level 2 → Locations 2 hops away
Level 3 → Locations 3 hops away
```

Therefore, when BFS first reaches the destination, it has used the minimum possible number of edges.

## Example

```text
Gate → Library → Canteen → Lab
```

The system identifies the route with the minimum number of hops.

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/campus-route-finder-bfs.git
```

Move into the project directory:

```bash
cd campus-route-finder-bfs
```

Run the program:

```bash
python src/campus_route_finder.py
```

## Testing

Run the test file using:

```bash
python tests/test_bfs.py
```

## Project Structure

```text
campus-route-finder-bfs/
│
├── src/
│   └── campus_route_finder.py
│
├── tests/
│   ├── test_bfs.py
│   └── sample_input.txt
│
├── docs/
│   ├── report.pdf
│   └── screenshots/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Results

The system successfully:

- Represents the campus as an unweighted graph.
- Finds the shortest route using BFS.
- Displays the complete path.
- Calculates the number of hops.
- Demonstrates that BFS produces the fewest-edge path.

## Applications

- Campus navigation
- Student route finding
- Visitor guidance
- Educational demonstration of graph algorithms
- Basic navigation systems

## Team Members

- Praveen S
- Tamilarasi M
- Vemula Harish S

## Department

Computer Science and Engineering  
Artificial Intelligence & Machine Learning

## Course

Foundations of Artificial Intelligence

## Conclusion

The Campus Route Finder Using BFS demonstrates the practical use of graph traversal for finding shortest routes.

BFS is suitable for an unweighted campus graph because it explores locations level by level and guarantees a path with the minimum number of edges.

The system provides a simple and effective way to find routes between campus locations.
