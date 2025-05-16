from trie import Trie

def main() -> None:
    trie = Trie()
    
    trie.inserts("alignment")
    trie.inserts("apples")

    assert trie.explores("alignment") == True, "miss `alignment`"

    assert trie.explores("apple") == False, "mismatch `apple` from `apples`"
    assert trie.explores("apples") == True, "miss `apples`"
    
    assert trie.explores("x") == False, "false search `x`"

    assert trie.explores("") == False, "false search ``"
    trie.inserts("")
    assert trie.explores("") == True, "miss ``"

    assert trie.explores("app.es") == True, "mismatch `app.es` from `apples`"
    assert trie.explores("..p.es") == True, "mismatch `..p.es` from `apples`"

    print("over success")


if __name__ == "__main__":
    main()
