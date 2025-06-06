import math

class Triplet:
    
    def __init__(self, left: int, midd: int, rite: int) -> None:
        self.triplet = [left, midd, rite]

    def __hash__(self) -> int:
        return hash(tuple(self.triplet))
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Triplet): return False
        return self.__hash__() == other.__hash__()

    def sums(self) -> int:
        return sum(self.triplet)


def finds_triplets(nums: list, target: int = 0) -> list[list[int]]:
    closest, length = math.inf, len(nums)
    candidates = list()
    visits = set()
    nums.sort()
    for left in range(length - 2):
        midd, rite = left + 1, length - 1
        while midd < rite:
            current = Triplet(nums[left] , nums[midd] , nums[rite])
            sumup = current.sums()
            distance = abs(target - sumup)
            if current not in visits:
                if distance < closest:
                    closest = distance
                    candidates = [current]
                if distance == closest and current not in candidates:
                    candidates.append(current)
                visits.add(current)
            if sumup <= target:
                tempa = nums[midd]
                while midd < rite and nums[midd] == tempa:
                    midd += 1
            else: 
                tempa = nums[rite]
                while midd < rite and nums[rite] == tempa:
                    rite -= 1
                    
    return [item.triplet for item in candidates]
