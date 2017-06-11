def which_prize(points):
    """
    Notifies a competitor of the prize they have won in a game,
    depending on the number of points they've scored
    """
    prize = "No prize"
    if <= 50:
        prize = "wooden rabbit"
    elif <= 150:
        prize = "No prize"
    elif <= 180:
        prize = "wafer-thin mint"
    elif <= 200:
        prize = "penguin"

    if prize == "No prize":
        return "Oh dear, no prize this time."
    else:
        return "Congratulations! You have won a {}!".format(prize)

print(which_prize(2000))
