from versioning_keyval import VersionKeyVal

def runs() -> None:
    verkyvl = VersionKeyVal()

    try:
        verkyvl.search("a")
    except KeyError:
        pass

    try: 
        verkyvl.delete("w")
    except KeyError:
        pass
    

    verkyvl.upsert("a", 1)
    verkyvl.upsert("b", 2)

    assert verkyvl.search("a") == 1, "failure in val fetch from curr hashmap storage"

    verkyvl.upsert("a", 50)
    assert verkyvl.search("a") == 50, "failure in val fetch after upsertion"
    

    snap1 = verkyvl.snapshot()
    
    assert verkyvl.search("b", snap1) == 2, "failure in val fetch from snap" + snap1

    try:
        res = verkyvl.search("b", snap1 - 1)
    except KeyError:
        pass

    snap2 = verkyvl.snapshot()
    
    assert verkyvl.search("b", snap2) == 2, "failure in val fetch from snap: " + snap2

    verkyvl.upsert("c", 120)
    assert verkyvl.search("c") == 120, "failure in val fetch from current hashmap storage"

    try:
        res = verkyvl.search("c", snap2)
    except KeyError:
        pass

    snap3 = verkyvl.snapshot()
    
    assert verkyvl.search("c", snap3) == 120, "failure in val fetch from snap: " + snap3

    verkyvl.delete("b")

    assert verkyvl.search("b", snap3) == 2, "failure in val fetch from snap: " + snap3 + "after deletion"

    try:
        res = verkyvl.search("b")
    except KeyError:
        pass

    snap4 = verkyvl.snapshot()
    
    try:
        res = verkyvl.search("b", snap4)
    except KeyError:
        pass

    verkyvl.upsert("b", 99)

    snap5 = verkyvl.snapshot()

    assert  verkyvl.search("b", snap5) == 99, "failure in val fetch from snap: "+ snap5

    print("success")


if __name__ == "__main__":
    runs()
