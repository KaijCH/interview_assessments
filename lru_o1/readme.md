# O1 LRU Cache

## Description

1. Designing `KeyValO1` class that fulfills LRU cache designs with max capacity of storage

2. Implementing get & set operation following requirements below

    > `search(key: str) -> tuple[str, bool]` returning `"", False` if key does not exist in cache otherwise `EXPECT_VAL, True`

    > `upsert(key: str, val: str)` upserting `key:val` pair to cache, evicting the least-recent-use `key:val` from cache if max capacity reaches

3. Getting & Setting operations should each take close to O(1) time and considered promoting the usage of the `key` in cache

## Inspiration

### How to maintain order or relationship of least-recent-usage for the O1 requirement

1. Using queue is not acceptable for least-recent-usage order since problem requires close to O(1) for get & set operations, what about LinkedList?

2. Storing the `key:LinkedListDataNode` instead of `key:val`, including the `key` in LinkedListDataNode to save eviction key retrieval

3. Avoiding enumeration-time by employing Bi-Directional-LinkedList, maintaining head & tail pointers to the LinkedList struct as well to save eviction time when capacity max out
