def coin(amt, denominations, index=0):

    if amt == 0:
        return 1

    if amt < 0:
        return 0

    if index == len(denominations):
        return 0

    current_coin = denominations[index]

    count = 0
    while amt >= 0:
        count += coin(
            amt,
            denominations,
            index + 1,
        )
        amt -= current_coin
    return count

print(coin(4,[1,2,3],0))
print(coin(0,[1,2],0))
print(coin(1,[],0))
print(coin(5,[25,50],0))
print(coin(50,[5,10],0))
