# Transaction ReMatch

## Descriptions

1. using dataset of transactions, orders, tickets (each in csv-like format, list), re-match transaction id back to useranme

2. assuming each user will place only 1 order, assuming all users will places 1 order each

3. explaining content of datasets:

    > orders: name, mail, label, count

    > tickets: label, value

    > transactions: id, total, mail

## Inspriations

### how to align between transactions and orders

1. using the `total` value of transactions and orders, considering the condition of problem states about relation between users & orders

### how to handle mail addr miss from transactions, and multi user place same total transactions

1. keeping separate lookups between total & name `{total:[name, name, ...]}` so that if mail legit the record is legit for return

2. discarding name from `{total:[name, name, ...]}` storage once record finds valid and enqueue for return, avoiding duplications

3. keeping a separate list of "miss mail transaction" `[(id, total)]` for final random assignment between name & transaction id
