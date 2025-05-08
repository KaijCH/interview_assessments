from rematch import *

def runs()-> None:
    # info: name, mail, label, count
    orders = [
        ["Alice", "alice@g.edu", "1", "3"],
        ["Heidi", "he@g.edu", "1", "3"],
        ["Eliza", "eliza@g.edu", "3", "1"],
        ["Peggi", "ie@g.edu", "1", "3"],
        ["Dinda", "da@g.edu", "2", "10"],
    ]
    # tickets: label, value
    tickets = [
        ["1", "10"],
        ["2", "20"],
        ["3", "100"],
    ]
    # transactions: id, total, mail
    transactions = [
        ["1", "30", "N/A"],
        ["2", "30", "alice@g.edu"],
        ["3", "100", "N/A"],
        ["4", "200", "N/A"],
        ["5", "30", "N/A"],
    ]

    # execute
    matches = rematch(orders=orders, transactions=transactions, tickets=tickets)
    matches = dict(matches)

    # validate
    assert matches["1"] in ["Peggi", "Heidi"], "err in transaction_id 1"
    assert matches["2"] == "Alice", "err in transaction_id 2"
    assert matches["3"] == "Eliza", "err in transaction_id 3"
    assert matches["4"] == "Dinda", "err in transaction_id 4"
    assert matches["5"] in ["Peggi", "Heidi"], "err in transaction_id 5"
    print(matches)


if __name__ == "__main__":
    """
        Implementing a re-match helper that uses transactions data and userinfo to retrieve relation: username <> transaction_id
            whenever a mail is missing from transactions dataset, as should properly deduce the username
            it is safe to assume all transaction_id has exactly 1 username relate to, and vice versa
            
    """
    runs()