import math
import pandas as pd
import unittest

# calculate drowdown, absolute(absolute difference of profit) or relative (relative to the deposit)
def DrowDown(orders, mode="abs"):
   
    max_DD = 0
    cur_DD = 0
    deposit = 0
    balance = 0
    max_balance = 0

    for i in range(len(orders)):
        # reset balance if deposit increase or decrease
        if mode=="abs":
            if orders['OpenType'][i] !=1 and orders['OpenType'][i] != 0:
                deposit+=orders['Profit'][i]
                balance = deposit
                max_balance = deposit
            else:
                balance+=orders['Profit'][i]
        else:
            balance+=orders['Profit'][i]

        # set max reached balance
        if balance>max_balance:
            max_balance=balance

        #  calculate drowdown
        if mode=="abs":
            cur_DD=max_balance-balance
        else:
            if max_balance-balance != 0 and max_balance != 0:
                cur_DD=(max_balance-balance)/max_balance*100
        
        if cur_DD>max_DD:
            max_DD=cur_DD

    return abs(max_DD)

# Z-score calculation
def ZScore( N, W, L, R):

    if N<3:
        return 0
    
    p = 2.0 * W * L
    numerator = (N * (R - 0.5) - p)
    denominator = math.sqrt((p * (p - N)) / (N - 1))
    if denominator != 0.0:
        return numerator / denominator
    
    return 0

# R calculation
def R(arr):

    R = 0
    for i in range(len(arr)):
        if i > 0:
            if (arr[i - 1] < 0 and arr[i] >= 0) or (arr[i - 1] > 0 and arr[i] <= 0):
                R += 1
    return R

# calculate main results (Profit, Trades, Buys, Sells, RiskReward, Z-score)
def Metrics(orders):
    
    # remove deposits
    orders = orders[orders['OpenType'].isin([0, 1])]

    # Initialize the result dictionary
    result = {'RR': None, 'Z-score': [], 'Profit': None, 'Trades': None, 'Buys': None, 'Sells': None}

    # Calculate profit
    result['Profit'] = orders['Profit'].sum().round(2)

    # Calculate number of trades
    result['Trades'] = orders['Profit'].count()

    # Count buy and sell orders
    buy_orders = orders[orders['OpenType'] == 0]
    sell_orders = orders[orders['OpenType'] == 1]
    result['Buys'] = buy_orders['OpenType'].count()
    result['Sells'] = sell_orders['OpenType'].count()

    # Calculate risk reward
    profit = orders[orders['Profit'] >= 0]['Profit'].sum()
    loss = orders[orders['Profit'] < 0]['Profit'].sum()
    if loss!=0:
        result['RR'] = abs(profit / loss).astype(float).round(decimals=2)
    else: 
        result['RR'] = 0 

    # Calculate and add Z-score
    trades = orders['Profit'].count()
    profit = orders[orders['Profit'] >= 0]['Profit'].count()
    loss = orders[orders['Profit'] < 0]['Profit'].count()
    r = R(orders['Profit'].to_numpy())
    result['Z-score'] = round(ZScore(trades, profit, loss, r),2)
    
    return result

# test
test_df = pd.DataFrame({
            'OpenType': [0, 1, 0, 1, 2, 0, 0, 1],
            'Profit': [10, -5, 15, -10, 100, -50, 20, -10]
        })
metrics = Metrics(test_df)
metrics["DD"] = DrowDown(test_df) 
print(metrics)

