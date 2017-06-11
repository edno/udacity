def which_prize(points):
    """
    Notifies a competitor of the prize they have won in a game,
    depending on the number of points they've scored
    """
    prize = None
    if points <= 50:
        prize = "wooden rabbit"
    elif points <= 150:
        prize = None
    elif points <= 180:
        prize = "wafer-thin mint"
    elif points <= 200:
        prize = "penguin"

    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."

print(which_prize(20))
