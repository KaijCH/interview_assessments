from message_deduplication import TestBed, deduplicates

def main() -> None:
    # empty message
    msgs = []
    test0 = TestBed(tests=msgs,  threshold=3)
    expt0 = []
    assert deduplicates(test0) == expt0, "failure in handling none message"
    
    # signle message
    msgs = [
        [0, "Low Power"]
    ]
    test1 = TestBed(tests=msgs,  threshold=1)
    expt1 = [[0, "Low Power"]]
    assert deduplicates(test1) == expt1, "failure in rendering single message"

    # multiple overlap message
    msgs = [
        [0, "Low Power"],
        [1, "High Temperature"],
        [2, "Low Power"],
        [7, "Low Power"],
        [12, "Low Power"],
        [13, "Out of Memory"],
        [14, "High Temperature"],
    ]
    test2 = TestBed(tests=msgs, threshold=10)
    expt2 = [[1, "High Temperature"],[12, "Low Power"],[13, "Out of Memory"],[14, "High Temperature"]]
    assert deduplicates(test2) == expt2, "failure in filtering duplication"

    print("overall success")


if __name__ == "__main__":
    main()