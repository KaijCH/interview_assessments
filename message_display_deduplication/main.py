from message_deduplication import TestBed, deduplicates

def main() -> None:
    msgs = [
        [0, "Low Power"],
        [1, "High Temperature"],
        [2, "Low Power"],
        [7, "Low Power"],
        [12, "Low Power"],
        [13, "Out of Memory"],
        [14, "High Temperature"],
    ]
    test1 = TestBed(msgs, 10)
    assert deduplicates(test1) == [[1, "High Temperature"],[12, "Low Power"],[13, "Out of Memory"],[14, "High Temperature"]]

    msgs = [
        [0, "Low Power"]
    ]
    test1 = TestBed(msgs, 10)
    assert deduplicates(test1) == [[0, "Low Power"]]

    print("overall success")


if __name__ == "__main__":
    main()