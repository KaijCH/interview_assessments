from o1_lru import KeyValO1


def main() -> None:

    o1lru = KeyValO1(3)
    res, has = o1lru.search("a")
    assert res == "" and has == False, "failure in retrieving non existence"

    o1lru.upsert("a", "1")
    res, has = o1lru.search("a")
    assert res == "1" and has == True, "failure in retrieving existence"

    o1lru.upsert("a", "2")
    res, has = o1lru.search("a")
    assert res == "2" and has == True, "failure in retrieving overriding val"

    for key, val in [["b", "2"], ["c", "3"], ["d", "4"]]:
        o1lru.upsert(key, val)
    res, has = o1lru.search("a")
    assert res == "" and has == False, "failure in evicting least recent usage"

    res, has = o1lru.search("b")
    assert res == "2" and has == True, "failure in evicting least recent usage"

    print("overall success")


if __name__ == "__main__":
    main()
