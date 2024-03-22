def net_amount(log):
    total = 0
    for transaction in log.split():
        amount = int(transaction[2:])
        if transaction[0] == 'D':
            total += amount
        else:
            total -= amount
    return total

transaction_log = "D 300 D 300 W 200 D 100"
net_amount_result = net_amount(transaction_log)
print(net_amount_result)
