# HashMap with Transaction

## Descriptions

1. implementing a HashMap class that support transaction operation: `upsert()`, `transact()`, `commit()`, `search()`

2. assuming invocation of `transact()` & `commit` is accessible in any point of time in rumtime

3. returning `-1` for key miss

## Inspriations

### how to keep `key-val` pair in transaction and not interfere with values outside of transaction

1. searching `key` only return `key:val` from the major (hashmap) storage

1. using a new separate hashmap to keep track of data changes in current transaction

2. assigning `key:val` from current transaction hashmap to either major hashmap or outer layer of transaction

3. handling nest-transactions by enqueuing all transaction hashmap to a stack, committing current transaction equal to assign all `key:val` pair from last hashmap to the one prior to it or to the major hashmap storage
