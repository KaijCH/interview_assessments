# HashMap with Snapshot

## Descriptions

1. Implementing a Hashmap class with Snapshot capabilities, that supports versioning retrieval of keys' value

> `upsert(key: str, val: int) -> None`: update & insert `key:val` pair to hashmap storage

> `search(key: str, vers: int = None) -> int`: search val by `key`, if `vers` specifies then retrieval perform among the snapshot version, raise KeyError if `key` misses or `vers` exceeds current snapshot version

> `delete(key: str) -> None`: delete `key` from current hashmap, raise KeyError if key misses

> `snapshot() -> int`: create version of current hashmap, return `snapshot id` in int starting from 0

2. Using as minimum as possible of space, and close to O(1) runtime for all operations: `delete()`, `search()`, `upsert()`, `snapshot()`

## Inspriations

### how to keep track of value changes across different snapshot version, with minimum space consumption

1. creating a incremental `{key:{ver:val}}` lookups for specific key histrial val retrieval, sync all operation of the primary `{key:val}` hashmpa to this lookups to minimize overall average single operation runtime

2. understanding that if no operation for key during any snapshots, the retrieval of histrial val should go backward by snapshot version

### how to handle deletion, how to distinguish a deletion from key miss

1. marking **deletion** of key with special identifier in the incremental hashmap storage
