from transacting_keyval import TxnKeyVal

def runs() -> None:
    # initialization
    txnkyvl = TxnKeyVal()

    # malicious invocation of commit before transaction starts
    txnkyvl.commit()

    # major map assignment & validation
    txnkyvl.upsert("a", 1)
    assert txnkyvl.search("b") == -1, "key miss err"
    txnkyvl.upsert("b", 10)
    assert txnkyvl.search("b") == 10, "val err"

    # single layer transaction & validation
    txnkyvl.transact()
    txnkyvl.upsert("a", 100)
    assert txnkyvl.search("a") == 1, "val misfetch in transaction"
    txnkyvl.commit()
    assert txnkyvl.search("a") == 100, "transaction fail commit"

    # multi layer transaction & validation
    txnkyvl.transact()
    txnkyvl.upsert("x", 92)
    txnkyvl.transact()
    txnkyvl.upsert("a", 200)
    assert txnkyvl.search("a") == 100, "val misfetch in transaction"
    assert txnkyvl.search("c") == -1, "val misfetch in transaction"
    txnkyvl.commit()
    assert txnkyvl.search("a") == 100, "val misfetch in transaction"
    txnkyvl.upsert("w", 32)
    txnkyvl.transact()
    txnkyvl.upsert("r", 64)
    txnkyvl.commit()
    txnkyvl.transact()
    txnkyvl.commit()
    assert txnkyvl.search("w") == -1,  "val misfetch in transaction"
    txnkyvl.commit()
    assert txnkyvl.search("r") == 64,  "transaction fail commit"
    assert txnkyvl.search("x") == 92,  "transaction fail commit"
    assert txnkyvl.search("w") == 32,  "transaction fail commit"

    print("success")


if __name__ == "__main__":
    runs()