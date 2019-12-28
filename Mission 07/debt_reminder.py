def give_money(borrowed_money, from_person, to_person, amount):
    if (type(amount) != int and type(amount) != float) or type(from_person) != str or type(to_person) != str or type(borrowed_money) != dict or from_person == to_person:
        raise ValueError
    if to_person in borrowed_money and from_person in borrowed_money[to_person]:
        borrowed_money[to_person][from_person] += amount
    elif to_person in borrowed_money and from_person not in borrowed_money[to_person]:
        borrowed_money[to_person][from_person] = amount
    else:
        borrowed_money[to_person] = {from_person:  amount}

    if from_person in borrowed_money and to_person in borrowed_money[from_person]:
        borrowed_money[from_person][to_person] -= amount
    elif from_person in borrowed_money and to_person not in borrowed_money[from_person]:
        borrowed_money[from_person][to_person] = -amount
    else:
        borrowed_money[from_person] = {to_person: -amount}


def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict:
        raise ValueError
    amount = 0
    for keys in borrowed_money:
        for keys2 in borrowed_money[keys]:
            if borrowed_money[keys][keys2] > 0:
                amount += borrowed_money[keys][keys2]
    return amount


borrowed_money = {}

give_money(borrowed_money, "Mark", "Bill", 2000000)
give_money(borrowed_money, "Mark", "Steve", 2000000)
give_money(borrowed_money, "Serguei", "Bill", 5000000)
give_money(borrowed_money, "Bill", "Larry", 6000000)
give_money(borrowed_money, "Larry", "Linus", 5.5)
give_money(borrowed_money, "Steve", "Mark", 2000000)

print(borrowed_money)
print(total_money_borrowed(borrowed_money))
