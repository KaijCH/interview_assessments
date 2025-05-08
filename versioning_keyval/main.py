from ver_keyval import VersionKeyVal

def runs() -> None:
    vkv = VersionKeyVal()

    try:
        vkv.search("a")
    except KeyError:
        print("search a key err", True)

    vkv.upsert("a", 1)
    vkv.upsert("b", 2)

    try:
        res = vkv.search("a")
    except KeyError:
        print("search a key err", False)
    print("search a == 1", res == 1)

    vkv.upsert("a", 50)
    try:
        res = vkv.search("a")
    except KeyError:
        print("search a key err", False)
    print("search a == 50", res == 50)

    snap1 = vkv.snapshot()
    print(vkv.persist, snap1)

    try:
        res = vkv.search("b", snap1)
    except KeyError:
        print("search b key err", False)
    print("search b snap1 == 2", res == 2)

    try:
        res = vkv.search("b", snap1 - 1)
    except KeyError:
        print("search b snap0 ver err", True)

    snap2 = vkv.snapshot()
    print(vkv.persist)

    try:
        res = vkv.search("b", snap2)
    except KeyError:
        print("search b snap2 ver err", False)
    print("search b snap2 == 2", res == 2)

    vkv.upsert("c", 120)
    try:
        res = vkv.search("c")
    except KeyError:
        print("search c key err", False)
    print("search c == 120", res == 120)

    try:
        res = vkv.search("c", snap2)
    except KeyError:
        print("search c snap2 ver err", True)

    snap3 = vkv.snapshot()
    print(vkv.persist)
    try:
        res = vkv.search("c", snap3)
    except KeyError:
        print("search c snap3 ver err", False)
    print("search c snap2 == 120", res == 120)

    vkv.delete("b")

    try:
        res = vkv.search("b", snap3)
    except KeyError:
        print("search c snap2 ver err", False)
    print("search b snap3 == 2", res == 2)

    try:
        res = vkv.search("b")
    except KeyError:
        print("search b ver err", True)

    snap4 = vkv.snapshot()
    print(vkv.persist)

    try:
        res = vkv.search("b", snap4)
    except KeyError:
        print("search b key err", True)


    vkv.upsert("b", 99)

    snap5 = vkv.snapshot()
    print(vkv.persist)

    try:
        res = vkv.search("b", snap5)
    except KeyError:
        print("search b key err", False)
    print("search b snap5 == 99", res == 99)


if __name__ == "__main__":
    runs()
