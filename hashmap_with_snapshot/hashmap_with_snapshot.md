# HashMap with Snapshot

## descriptions

1. implementing a Hashmap class with Snapshot capabilities, that supports versioning retrieval of keys' value

2. raising KeyError when key is miss from KeyVal strorage

3. using as minimum as possible of space, and close to O(1) runtime for all operations: `delete()`, `search()`, `upsert()`, `snapshot()`

## inspriations

### how to keep track of value changes across different snapshot version, with minimum space consumption

1. creating a incremental `{key:{ver:val}}` lookups for specific key histrial val retrieval, sync operation of this lookups with the major `{key:val}` storage

2. understanding that if no operation for key during any snapshots, the retrieval of histrial val should go backward by snapshot version

### how to handle to deletion, how to distinguish a deletion from key miss

1. marking **deletion** of key with special identifier in the incremental historial storage
