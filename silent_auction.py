bids = {}


def try_float(number):
    """
    This function will try to convert the input to a float.
    If it is not a float it will return False.
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


def silent_bid():
    """collect the silent bids"""
    name = input("What is your name? ").title()
    if name == "F":
        return "F"
    bid = input("What is your bid? ")
    while not try_float(bid) or float(bid) < 0:
        bid = input("What is your bid? ")



def main():
    """
    run the main part of the code
    """
    reserve = input("What is the reserve price? ")
    while not try_float(reserve) or float(reserve) < 0:
        reserve = input("What is the reserve price? ")
    print("Auction has started")
    fail_test = silent_bid()
    while fail_test != "F":
        fail_test = silent_bid()


main()
