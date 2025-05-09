# HashMap with Transaction

## Descriptions

1. implementing a HashMap class that support transaction operation:

    > `upsert(key: str, val:int) -> None`: insert & update key-val pair to current writing transaction or major storage

    > `search(key: str) -> int`: search key from major hashmap, return `-1` for key miss

    > `transact() -> None`: create a transaction, prepare for batch apply changes once

    > `commit() -> bool`: commit changes in current transaction, return `True` if successful, `Fasle` if no transaction to commit

    > `rollback() -> bool`: rollback current transaction, return `True` if successful, `Fasle` if no change to rollback

2. requiring current transaction operations are not affecting the outside values unless `commit()` calls

3. assuming invocation of `transact()` & `commit` is accessible in any point of time in rumtime

## Inspriations

### how to keep `key-val` pair in transaction and not interfere with values outside of transaction

1. searching `key` only return `key:val` from the major (hashmap) storage

2. using a new separate hashmap to keep track of data changes in current transaction

3. assigning `key:val` from current transaction hashmap to either major hashmap or outer layer of transaction

4. handling nest-transactions by enqueuing all transaction hashmap to a stack, committing current transaction equal to assign all `key:val` pair from last hashmap to the one prior to it or to the major hashmap storage
