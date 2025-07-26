import heapq

def find_number(strin: str, largest: int) -> int:
    numbers = strin.split(" ")
    numba = list()
    for elem in numbers:
        if not elem.isdigit():
            continue
        num = -int(elem)
        heapq.heappush(numba, num)
    while numba and largest:
        largest -= 1
        num = heapq.heappop(numba)
        if largest == 0:
            return -num
    
    return -1
