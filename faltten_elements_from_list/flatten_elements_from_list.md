# Flatten Elements from List

## Description

1. implementing `flattens(elements: list)` function which serve flattening all elements from in given nested list `elements`

2. securing the function so that it withstands the recursive array or empty element

```[]Python
    # example of constructing a recursive arr
    arr = [1, 2]
    arr[0] = arr

```

## Inspriation

### How to handle the recursive arr case

1. keeping a hashset for all elements' reference, including the list itself

2. checking current element' reference, ignoring current element if found in reference hashset
