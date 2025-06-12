# Trie with Wildcard

## Description

- Implementing a Trie to fulfil the upsert, search of words

    > `explores(word: str) -> bool`, return truthy of whether `word` exist in current trie

    > `inserts(word: str) -> None`, fulfill insertion of current `word`

    > 0 <= len(word) < 10 ** 4

- Supporting `.` & `*` wildcards in words' exploration behaves similarly to RegEx

    > explores("apples") == explores(".pples") == explores("a.\*les") == explores("apples.\*")

## Inspriations

### how to match Wildcard in search

1. Employing Depth-First Search or Breadth-First Search, building node for each search by `(sub-trie-layer, index-in-search-pattern)`

2. Including all subsequent sub-trie from current layer, once `wildcard` appears

3. Ignoring any mismatch of current `char` from sub-trie, continuing next sub-trie match attempt, rather than of early return

4. Using Depth-Frist Search might better benefitting the cache/memorization of search attempts

### how to determine ending of word search

1. Marking tail of word insertion with special mark like `"#"`: `"#" = {}`

2. Using `{}` s value of ending `layer` in avoiding potential NULL pointer error

3. Mismatching `char` from any level of search results in overall either empty `searches` stack/queue, or char index incomplete, checking both conditions for truthy return

### how to handle potential consecutive char vs dot-star wildcard senario

1. Checking `idx` & `idx+1` during char enumeration from `word` to see if `*` exists

2. Exhausting different depth of `sublayer` with same `char`, iterating by `sublayer = sublayer[char]` Depth-First Search, building nodes for all potential match case
