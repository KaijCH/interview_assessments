from hashmap_snapshot.versioning_keyval import VersionKeyVal

def runs() -> None:
    verkyvl = VersionKeyVal()

    try:
        verkyvl.search("a")
    except KeyError:
        print("search a key err", True)

    verkyvl.upsert("a", 1)
    verkyvl.upsert("b", 2)

    try:
        res = verkyvl.search("a")
    except KeyError:
        print("search a key err", False)
    print("search a == 1", res == 1)

    verkyvl.upsert("a", 50)
    try:
        res = verkyvl.search("a")
    except KeyError:
        print("search a key err", False)
    print("search a == 50", res == 50)

    snap1 = verkyvl.snapshot()
    print(verkyvl.persist, snap1)

    try:
        res = verkyvl.search("b", snap1)
    except KeyError:
        print("search b key err", False)
    print("search b snap1 == 2", res == 2)

    try:
        res = verkyvl.search("b", snap1 - 1)
    except KeyError:
        print("search b snap0 ver err", True)

    snap2 = verkyvl.snapshot()
    print(verkyvl.persist)

    try:
        res = verkyvl.search("b", snap2)
    except KeyError:
        print("search b snap2 ver err", False)
    print("search b snap2 == 2", res == 2)

    verkyvl.upsert("c", 120)
    try:
        res = verkyvl.search("c")
    except KeyError:
        print("search c key err", False)
    print("search c == 120", res == 120)

    try:
        res = verkyvl.search("c", snap2)
    except KeyError:
        print("search c snap2 ver err", True)

    snap3 = verkyvl.snapshot()
    print(verkyvl.persist)
    try:
        res = verkyvl.search("c", snap3)
    except KeyError:
        print("search c snap3 ver err", False)
    print("search c snap2 == 120", res == 120)

    verkyvl.delete("b")

    try:
        res = verkyvl.search("b", snap3)
    except KeyError:
        print("search c snap2 ver err", False)
    print("search b snap3 == 2", res == 2)

    try:
        res = verkyvl.search("b")
    except KeyError:
        print("search b ver err", True)

    snap4 = verkyvl.snapshot()
    print(verkyvl.persist)

    try:
        res = verkyvl.search("b", snap4)
    except KeyError:
        print("search b key err", True)


    verkyvl.upsert("b", 99)

    snap5 = verkyvl.snapshot()
    print(verkyvl.persist)

    try:
        res = verkyvl.search("b", snap5)
    except KeyError:
        print("search b key err", False)
    print("search b snap5 == 99", res == 99)


if __name__ == "__main__":
    runs()
