# Sum of triplets closest to target

## Description

1. Implementing `finds_triplets(nums: list, target: int)` function, finding all unique triplets from given `nums` arr, satisfying condition that triplets' sum are closest to the given `target` integer

## Inspiration

### How to narrowing down the search space

1. Narrowing the search space of two pointers by enmerating the left pointer from 0 to length - 1 (just like normal 3Sum problem)

2. Ignoreing candidates with larger distance to `target`, in greedily update
