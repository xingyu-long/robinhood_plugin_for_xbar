#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# <xbar.title>Fancy Robinhood</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Xingyu Long</xbar.author>
# <xbar.author.github>xingyu-long</xbar.author.github>
# <xbar.desc></xbar.desc>
# <xbar.image></xbar.image>
# <xbar.dependencies>python,robin_stocks</xbar.dependencies>
import os

import robin_stocks.robinhood as r


GREEN = '\033[32m'
RED = '\033[1;31m'
DEFAULT_COLOR = '\033[0m'
FONT = "| font='Menlo'"


def get_colored_status(change):
    status = ''
    if change < 0:
        status = RED + '▼'
    elif change > 0:
        status = GREEN + '▲'
    return status


def return_equity_and_market_value():
    portfolio = r.profiles.load_portfolio_profile()
    current_value = portfolio['equity']
    open_value = portfolio['equity_previous_close']

    change = float(current_value) - float(open_value)
    change_in_percentage = change / float(open_value) * 100
    status = get_colored_status(change)
    total_change_info = "{:,.2f} {} {:,.2f}({:.2f}%)" + DEFAULT_COLOR
    print(total_change_info.format(float(current_value), status,
                                   abs(float(change)), change_in_percentage))
    return float(portfolio["equity"]), float(portfolio["market_value"])


def show_postions_as_list(equity, market_value):
    # Use '---' to represent the list will show below.
    print("---")
    stock_info = "{:<10} {:<10} {:<10} {:<20}" + DEFAULT_COLOR + FONT
    print(stock_info.format("Symbol", "Equity", "Allocation", "Total"))
    my_stocks = r.account.build_holdings()
    cash_position = round(equity - market_value, 2)
    cash_percentage = round(cash_position / equity * 100, 2)
    for stock_name, values in sorted(my_stocks.items(),
                                     key=lambda kv: kv[1]["percentage"],
                                     reverse=True):
        total_change = float(values["percent_change"])
        status = get_colored_status(total_change)
        change_with_status = status + " " + str(abs(total_change)) + "%"

        allocation = round(float(values["equity"]) / equity * 100, 2)
        print(stock_info.format(stock_name, values["equity"],
                                str(allocation) + "%", change_with_status))
    print(stock_info.format("Cash", str(cash_position), str(cash_percentage) + "%", "---"))


def main():
    username = os.environ["ROBINHOOD_USERNAME"]
    password = os.environ["ROBINHOOD_PASSWORD"]
    r.login(username, password)
    equity, market_value = return_equity_and_market_value()
    show_postions_as_list(equity, market_value)


if __name__ == '__main__':
    main()
