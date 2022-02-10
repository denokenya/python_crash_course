
def profit(buying_price, selling_price):
    """
       Desc: This module is used to calucate the profit of items
        params:buying_price ,selling_price

        print value : profit if selling_price is greater than buying_price
                     : loss if selling_price is less than buying_price

    """
    if selling_price > buying_price:

        profit = selling_price - buying_price
        print(f"You have made a profit of : Ksh {profit}")
    else:
        loss = buying_price - selling_price
        print(f"You have made a loss of : Ksh {loss}")
