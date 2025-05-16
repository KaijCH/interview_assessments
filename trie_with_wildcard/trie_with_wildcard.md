# Trie with Wildcard

## Description

- implementing a Trie to fulfil the insertion and observation of input word

    > explores(word: str) -> bool, return truthy of whether `word` exist in current trie

    > inserts(word: str) -> None, fulfill insertion of current `word`

- the exploration of word supports `.` wildcard, each wildcard equal to any single valid char

    > explores("apples") == explores(".pples")

- 0 <= len(word) < 10 ** 4

## Inspriations

### how to match Wildcard in search

1. employing BFS in sub-trie explorations rather than DFS

2. including all subsequent sub-trie from current layer, once `wildcard` appears

3. ignoring any mismatch of current `char` from sub-trie, continuing next sub-trie match attempt, rather than of early return

### how to determine ending of word search

1. marking tail of word insertion with special mark, like "#"

2. mismatching any `char` from all sub-trie will results in either empty `searches` queue or char index incomplete, checking both conditions
