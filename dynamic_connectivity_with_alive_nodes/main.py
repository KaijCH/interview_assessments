from dynamic_connection import DynamicConnect


def main():
    dc = DynamicConnect(10)

    dc.activates(0)
    dc.activates(1)    
    dc.activates(2)

    assert dc.connected(9, 6) == False, "failure in read connectivity over deactivate nodes"

    assert dc.connected(0, 1) == False, "failure in read connectivity over activate nodes"

    dc.connects(0, 1)

    assert dc.connected(0, 1) == True, "failure in read connectivity over activate nodes"

    dc.connects(1, 2)

    assert dc.connected(0, 2) == True, "failure in read connectivity over relay nodes"

    dc.deactivates(2)

    assert dc.connected(0, 2) == False, "failure in read connectivity over deactiviate nodes"

    dc.deactivates(0)

    assert dc.counts() == 1, "failure in count graph components"

    print("overall success")


if __name__ == "__main__":
    main()