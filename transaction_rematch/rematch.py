import collections

def rematch(orders: list, transactions: list, tickets: list) -> list:
    NotAvailable = "N/A"
    label2value = dict()
    for label, value in tickets:
        label2value[label] = int(value)

    mail2name, total2names = dict(), dict()

    for name, mail, label, count in orders:
        mail2name[mail] = name
        total = label2value[label] * int(count)
        if total not in total2names:
            total2names[total] = set()
        total2names[total].add(name)
    
    matches, misses = list(), list()
    transactions = collections.deque(transactions)
    while transactions:
        current = transactions.popleft()
        iden, total, mail = current
        total = int(total)
        if mail != NotAvailable and mail in mail2name:
            name = mail2name[mail]
            record = (iden, name)
            total2names[total].remove(name)
            matches.append(record)
            continue
        candidates = total2names[total]
        if len(candidates) != 1:
            miss = (iden, total)
            misses.append(miss)
            continue
        name = total2names[total].pop()
        record = (iden, name)
        matches.append(record)
    
    for iden, total in misses:
        name = total2names[total].pop()
        record = (iden, name)
        matches.append(record)
    
    return matches
