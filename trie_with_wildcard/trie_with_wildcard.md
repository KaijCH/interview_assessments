# Trie with Wildcard

## Description

- implementing a Trie to fulfil the upsert, search of words

    > explores(word: str) -> bool, return truthy of whether `word` exist in current trie

    > inserts(word: str) -> None, fulfill insertion of current `word`

- the exploration of word supports `.` & `*` wildcards, behaves similarly to RegEx

    > explores("apples") == explores(".pples") == explores("a.\*les") == explores("apples.\*")

- 0 <= len(word) < 10 ** 4

## Inspriations

### how to match Wildcard in search

1. employing Depth-First Search or Breadth-First Search, building node for each search by `(sub-trie-layer, index-in-search-pattern)`

2. including all subsequent sub-trie from current layer, once `wildcard` appears

3. ignoring any mismatch of current `char` from sub-trie, continuing next sub-trie match attempt, rather than of early return

4. using Depth-Frist Search might better benefitting the cache/memorization of search attempts

### how to determine ending of word search

1. marking tail of word insertion with special mark like `"#"`: `"#" = {}`

2. using `{}` s value of ending `layer` in avoiding potential NULL pointer error

3. mismatching `char` from any level of search results in overall either empty `searches` stack/queue, or char index incomplete, checking both conditions for truthy return

### how to handle potential consecutive char vs dot-star wildcard senario

1. checking `idx` & `idx+1` during char enumeration from `word` to see if `*` exists

2. exhausting different depth of `sublayer` with same `char`, iterating by `sublayer = sublayer[char]` Depth-First Search, building nodes for all potential match case
