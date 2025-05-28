from trie import Trie

def main() -> None:
    trie = Trie()
    
    trie.inserts("alignment")
    trie.inserts("apples")

    assert trie.explores("alignment") == True, "miss `alignment`"
    assert trie.explores("apple") == False, "mismatch `apple` from `apples`"
    assert trie.explores("apples") == True, "miss `apples`"
    assert trie.explores("xt") == False, "false search `x`"

    assert trie.explores("") == False, "false search ``"
    trie.inserts("")
    assert trie.explores("") == True, "miss ``"

    assert trie.explores("app.es") == True, "mismatch `app.es` from `apples`"
    assert trie.explores("..p.es") == True, "mismatch `..p.es` from `apples`" 
    assert trie.explores("alignment.*") == True, "mismatch `alignment.*` from `alignment`"
    

    assert trie.explores("a.*les") == True, "mismatch `a.*les` from `apples`"
    assert trie.explores("a.*ples") == True, "mismatch `a.*ples` from `apples`"
    assert trie.explores("a.*.*les") == True, "mismatch `a.*.*les` from `apples`"
    assert trie.explores(".*apples") == True, "mismatch `.*apples` from `apples`"
    assert trie.explores(".*a.*les.*") == True, "mismatch `.*a.*les.*` from `apples`"
    assert trie.explores("..*.*..") == True, "mismatch `..*.*..` from `apples`"
    assert trie.explores("apdles") == False, "false match `apdles` from `apples`"

    trie.inserts("apes")

    assert trie.explores("apes"), "miss `apes`"
    assert trie.explores("a.*.*s") == True, "mismatch `a.*.*s` from `apes`"
    assert trie.explores("ap.*") == False, "mismatch `ap.*` from `apes`"
    assert trie.explores("....") == True, "miss `....` from `apes`"

    trie.inserts("exxxxxxxxert")
    assert trie.explores("exxxxxxxxert") == True, "miss `exxxxxxxxert`"
    assert trie.explores("e.*xxxxxxxert") == True, "mismatch `e.*xxxxxxxert` from `exxxxxxxxert`"
    assert trie.explores("e.*.*xxxxxxert") == True, "mismatch `e.*.*xxxxxxert` from `exxxxxxxxert`"
    assert trie.explores("e.*.*.*xxxxxert") == True, "mismatch `e.*.*.*xxxxxert` from `exxxxxxxxert`"
    assert trie.explores("e.*.*.*.*xxxxert") == True, "mismatch `e.*.*.*.*xxxxert` from `exxxxxxxxert`"
    assert trie.explores("e.*.*.*.*x.*xxert") == True, "mismatch `e.*.*.*.*x.*xxert` from `exxxxxxxxert`"

    assert trie.explores("a.*") == False, "false match `a.*`"
    trie.inserts("a")
    assert trie.explores("a.*") == True, "miss `a.*` from `a`"
    assert trie.explores(".*") == True, "miss `.*` from `a`"

    print("over success")


if __name__ == "__main__":
    main()
