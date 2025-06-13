# Transaction ReMatch

## Descriptions

1. Using dataset of transactions, orders, tickets (each in csv-like format, list), re-match transaction id back to useranme
    
    > orders: name, mail, label, count

    > tickets: label, value

    > transactions: id, total, mail

2. Assuming each user will place only 1 order, assuming all users will places 1 order each

## Inspriations

### how to align between transactions and orders

1. using the `total` value of transactions and orders, considering the condition of problem states about relation between users & orders

### how to handle mail addr miss from transactions, and multi user place same total transactions

1. Keeping separate lookups between total & name `{total:[name, name, ...]}` so that if mail legit the record is legit for return

2. Discarding name from `{total:[name, name, ...]}` storage once record finds valid and enqueue for return, avoiding duplications

3. Keeping a separate list of "miss mail transaction" `[(id, total)]` for final random assignment between name & transaction id
