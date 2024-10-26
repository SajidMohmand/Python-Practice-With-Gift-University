'''Stock Transation Program
Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
* The number of shares that Joe purchased was 2,000. * When Joe purchased the stock, he paid
40.00 Dollar per share. * Joe paid his stockbroker a commission that amounted to 3 percent of the
amount he paid for the stock.
Two weeks later Joe sold the stock. Here are the details of the sale: * The number of shares that
Joe sold was 2,000. * He sold the stock for 42.75 Dollar per share. * He paid his stockbroker
another commission that amounted to 3 percent of the amount he received for the stock.
Write a program that displays the following information: * The amount of money Joe paid for the
stock. * The amount of commission Joe paid his broker when he bought the stock. * The amount
that Joe sold the stock for. * The amount of commission Joe paid his broker when he sold the
stock. * Display the amount of money that Joe had left when he sold the stock and paid his broker
(both times). If this amount is positive, then Joe made a profit. If the amount is negative, then
Joe lost money.'''

shares = 2000

purchase_shares_amount = 40*shares
purchase_commission = 3/100 *purchase_shares_amount

sold_shares_amount = 42.75*shares
sold_commission = 3/100 * sold_shares_amount



left_amount = (sold_shares_amount-sold_commission)-(purchase_shares_amount+purchase_commission)

print()
print(sold_shares_amount+sold_commission)
print("Amount paid for stock : ",purchase_shares_amount)
print("Amount gain in sold stock : ",sold_shares_amount)
print("Broker commission in purchase stock : ",sold_commission)
print("Broker commission in sold stock : ",purchase_commission)
print("Amount of money joe left : ",left_amount)
if left_amount < 0:
    print("Joe loss amount")
else:
    print("Joe gain profit")



  