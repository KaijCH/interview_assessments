# Sum of triplets closest to target

## Description

1. implementing `finds_triplets(nums: list, target: int)` function, finding all unique triplets from arr `nums` with each of triplet's sum closest to the given `target`

## Inspiration

### How to narrowing down the search space

1. Narrowing the search space of two pointers by enmerating the left pointer from 0 to length - 1 (just like normal 3Sum)

2. Ignoreing candidates with larger distance to `target`, in greedily update
