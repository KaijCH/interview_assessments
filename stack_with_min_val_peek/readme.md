# Stack with Min Val Peek

## Description

1. Designing a `MinimaStack` that supports normal stack operation, and peek to min val of the stack

    > `MinimaStack()` initializing the stack instance

    > `push(val: int) -> None` pushing val to stack

    > `pop() -> int` removing and returning val from top of stack

    > `top() -> int` peeking top element from stack

    > `getMin() -> int` returning min val from stack

2. Implementing solution with  O(1) complexity for all function

3. Assuming no invalid operation will be performed in testcases

## Inspriation

### How to fetch min val fom stack with O(1) complexity

1. Fetching the min val from stack with `min()` interfance consumes O(N) time for it visits every element from stack

2. Keeping the "current min val" along with the current val while the `push()` operation seems more feasible
