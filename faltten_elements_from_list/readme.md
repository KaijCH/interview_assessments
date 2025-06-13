# Flatten Elements from List

## Description

1. Implementing `flattens_iterative(elements: list)` & `flattens_recursive(elements: list)` functions which each serve flattening all elements in the given nested list `elements`, using recursive or intertive logic

2. Securing the functions so that they endure the cyclic array like below

    ```[]Python
        # example of constructing a recursive arr
        arr = [1, 2]
        arr[0] = arr

    ```

## Inspriation

### How to handle the cyclic array case

1. Keeping a hashset for all elements' reference, including the list itself

2. Checking current element' reference, ignoring current element if found in reference hashset
