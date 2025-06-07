# Message Deduplication

## Description

1. Implementing the `deduplicates()` function, which fulfills deduplication of messages content generated from `Testcase.fetch_latest()` function, within given `threshold` time (in second)

2. Checking messages' exhaustiveness by `Testcase.continues() -> bool`, this function returns `False` if no more message availabile

3. Ignoring all message if duplication happens within `threshold` seconds

4. Referring to `Message` class for more detail

5. Displaying of message should be thru `Message.displays()`, and return a list of filtered message


## Inspiration

## How to organize the relation between Message instance and Time to present

1. Using a hashtable, with key as message content, and val as expiration of such message's hold back threshold, in other waord: `{message: time + threshold}`

## How to recall a message if successor message form duplication within given threshold

1. Displaying a message does not need to be in realtime, holding a message back till threshold exceeds is relatively acceptable

2. Using a separate hashtable to track relation between timeframe (in seconds) and message that stands valid

3. Consuming message in every second of timeframe should be followed with a expiration check; Displaying message that passed the duplication expiration

4. Keeping extra while-loop after message generation stops
