# Flatten Elements from List

## Description

1. Implementing `flattens(elements: list)` function which serve flattening all elements from in given nested list `elements`

2. Securing the function so that endures the cyclic array like below

    ```[]Python
        # example of constructing a recursive arr
        arr = [1, 2]
        arr[0] = arr

    ```

3. (Follow-up) Implementing in both iterative and recursive

## Inspriation

### How to handle the recursive arr case

1. keeping a hashset for all elements' reference, including the list itself

2. checking current element' reference, ignoring current element if found in reference hashset
