def fine(authorized_speed, actual_speed):
    difference = actual_speed - authorized_speed
    price = 12.5
    if 2 < difference <= 10:
        price = difference * 5
    elif 10 < difference:
        price = difference * 5 * 2
    elif difference <= 0:
        price = 0
    return price
