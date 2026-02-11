# Settle Curior Payment

## Description

1. Given list of a curior's activities: `[[delivery_id, status, update_time], ...]` , and pay-per-minute rate, calculate how much should be paid to a that curior

2. The `delivery_id` uniquely identify each delivery order

3. The `update_time` is a string that follows format of `%Y-%m-%d %H:%M:%S`

4. The  `status` param is an enum and range within `cancel, complete, initiate`

5. For multime delivery order that go on simultaneously, `rate` should be multiply with the overlapping order count
