'''
The cost of stock on each day is given in an array A[] of size N. 
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day) For each input

'''
# Solution

'''
using greedy algorithm approach

The key idea behind the greedy algorithm in this code is to look for a local maximum (the best sell day) 
that is immediately followed by a local minimum (the best buy day), and repeat this process until all days have been processed.

Time: O(n)
Space: O(n)

'''
class Solution:
    def stockBuySell(self, price, n):
        #  if there is only one day in the stock prices, in which case print No Profit and return
        if n == 1:
            print("No Profit")
            return

        i = 0 # to keep track of the current day 
        transactions = [] # to store the best buy and sell days


        # for each day 
        while i < n - 1:
            # find best buy day by checking if next day's price greater than the current day's stock price, then the current day is the best buy day

            while i < n - 1 and price[i+1] <= price[i]:
                i += 1

            
            if i == n - 1:
                break

            buy = i

            i += 1

            # find best sell day by checking if next day's stock price is less than the current day's stock price, then the previous day is the best sell day

            while i < n and price[i] >= price[i-1]:
                i += 1

            sell = i - 1

            transactions.append((buy, sell))

        # If there are any transactions in the transactions list, print them out, otherwise print No Profit
        if transactions:
            for buy, sell in transactions:
                print("({} {})".format(buy, sell), end=" ")
            print()

        else:
            print("No Profit")




ob = Solution()
ans = ob.stockBuySell(price=[100, 180, 260, 310, 40, 535, 695], n=7)
print(ans)