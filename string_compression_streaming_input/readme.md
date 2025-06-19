# String Compression with Streaming Inout

## Description

1. Implementing `Compressor` class that supports streaming string compression with description below:

    > `compress(self, strin: str) -> str` returning compressing result that supports streaming input

    ```[]Python3
        compr.compress("a") => returns compression of "a"
        compr.compress("b") => returns compression of "ab"
    ```

    > `reset(self) -> None` resetting previous streaming inputs

2. Assuming that input will be always valid and within range: `a~zA~Z, 0~9`

## Inspiration

### How to compress digit in input

1. Using encode escaper like "_" or "\" to help representation

2. Using object-oriented design to help separate each symbols' representation from persistence

### How to handle and optimize streaming of input

1. Using stack/list to maintain previous streaming inputs in chunks

2. Using separate class var to keep track if last symbol in prev streaming input
