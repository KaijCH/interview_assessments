# Network Peer Contribution

## Description

0. Supposing a network, `NetworkServer` exists and dispatches chunks of data (with unique id) to different `NetworkPeer` instances; Measuring each `NetworkPeer` instances' contribution by direct + indirect involvement of chunks transmission like example below;

    ```Python3

    # Assume peers: A, B, C, D
    # Assume chunks 1, 2, 3, 4
    # Assume Server sends chunks [1,2] to A & chunks [3,4] to C

    # A sends [1, 2] to B
    # A sends [1] to C
    # C sends [4] to D
    # C sends [3] to B
    # B sends [3] to D
    # D sends [3] to A

    # A's total contribution should be 30 (MB)
    # B's total contribution should be 20
    # C's total contribution should be 40
    # D's total contribution should be 10
    # rank_vehicles should return [C,A,B,D]

    ```

1. Implementing function `NetworkServer.record_chunk_transaction()` to persist network peer interactions

2. Implementing function `NetworkServer.rank_vehicles()` that yeilds a list of peer's contribution, in desc order

3. (Follow-up) Providing the difference between total peer-to-peer contribution value and if direct-distributes to all peer instances

## Inspriation

### How to record transmission and how to rank between different peer instances

1. Implementing a "write-friendly" solution instead of "read-friendly" one, meaning we can only track down sender::receiver relation in `record_chunk_transaction()`, leaving the ranking calculation to the `rank_peers()`

2. Using adjacent list for sender::receiver relation, tracking `chunk_id` during records update in case same chunk might be sourced from multiple sender

### How to calculate rank score of all peer instances

1. Employing BFS search among sender::receiver adjacent list, tracking sender iteratively till sender is in chunk distribution register table

2. Using separate hashtable to increase all sender's score, sorting in reverse order
