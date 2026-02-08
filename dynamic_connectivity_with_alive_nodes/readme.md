# Dynamic Connectivity with Alive Nodes

## Description

1. Design a data structure to maintain an undirected graph of N nodes, where each node has a boolean 'alive' flag. Support the following operations efficiently for up to 100,000 operations:

    > `activates(i) -> None` / `deactivates(i) -> None` to toggle a node's alive status;

    > `connects(u, v)` that adds an edge only if both endpoints are currently alive;

    > `disconnects(u, v)` to remove an existing edge;

    > `connected(u, v) that returns whether u and v are in the same connected component considering only alive nodes; 

    > `counts()` to count over alive and connected components;


2. Discuss the time & space complexity of solution
