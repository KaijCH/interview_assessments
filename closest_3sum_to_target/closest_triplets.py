import math


def finds_triplets(nums: list, target: int = 0) -> list[list[int]]:
    closest, length = math.inf, len(nums)
    candidates = list()
    nums.sort()
    for left in range(length - 2):
        midd, rite = left + 1, length - 1
        while midd < rite:
            current = [nums[left] , nums[midd] , nums[rite]]
            sumup = sum(current)
            distance = abs(target - sumup)
            if distance < closest:
                closest = distance
                candidates = [current]
            if distance == closest and current not in candidates:
                    candidates.append(current)
            if sumup <= target:
                tempa = nums[midd]
                while midd < rite and nums[midd] == tempa:
                    midd += 1
            else: 
                tempa = nums[rite]
                while midd < rite and nums[rite] == tempa:
                    rite -= 1
                
    return candidates
