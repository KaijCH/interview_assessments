from transacting_keyval import TxnKeyVal

def runs() -> None:
    # initialization
    txnkyvl = TxnKeyVal()

    # malicious invocation of rollback before transaction starts
    assert txnkyvl.rollback() == False, "malicious success transaction rollback"

    # malicious invocation of commit before transaction starts
    assert txnkyvl.commit() == False, "malicious success transaction commit"

    # major map assignment & validation
    txnkyvl.upsert("a", 1)
    assert txnkyvl.search("b") == -1, "key miss err"
    txnkyvl.upsert("b", 10)
    assert txnkyvl.search("b") == 10, "val fetch err"

    # single layer transaction & validation
    txnkyvl.transact()
    txnkyvl.upsert("a", 100)
    assert txnkyvl.search("a") == 1, "val misfetch in transaction"
    assert txnkyvl.commit() == True, "failure in transaction commit"
    assert txnkyvl.search("a") == 100, "transaction fail commit"

    # multi layer transaction & validation
    txnkyvl.transact()
    txnkyvl.upsert("x", 92)
    txnkyvl.transact()
    txnkyvl.upsert("a", 200)
    assert txnkyvl.search("a") == 100, "val misfetch in transaction"
    assert txnkyvl.search("c") == -1, "val misfetch in transaction"
    assert txnkyvl.commit() == True, "failure in transaction commit"
    assert txnkyvl.search("a") == 100, "val misfetch in transaction"
    txnkyvl.upsert("w", 32)
    txnkyvl.transact()
    txnkyvl.upsert("r", 64)
    assert txnkyvl.commit() == True, "failure in transaction commit"
    txnkyvl.transact()
    assert txnkyvl.commit() == True, "failure in transaction commit"
    assert txnkyvl.search("w") == -1,  "val misfetch in transaction"
    assert txnkyvl.commit() == True, "failure in transaction commit"
    assert txnkyvl.search("r") == 64,  "transaction fail commit"
    assert txnkyvl.search("x") == 92,  "transaction fail commit"
    assert txnkyvl.search("w") == 32,  "transaction fail commit"

    # single layer upsertion & rollback
    txnkyvl.transact()
    txnkyvl.upsert("r", 32)
    assert txnkyvl.rollback() == True, "failure in rollback changes in current transaction"
    assert txnkyvl.commit() == False, "malicious success transaction commit"

    # multi layer upsertion & rollback
    txnkyvl.transact()
    txnkyvl.upsert("t", 21)
    txnkyvl.transact()
    txnkyvl.upsert("t", 41)
    assert txnkyvl.rollback() == True, "failure in rollback changes in current transaction"
    assert txnkyvl.commit() == True, "failure in current transaction commit"
    assert txnkyvl.search("t") == 21, "val fetch err"

    print("success")


if __name__ == "__main__":
    runs()