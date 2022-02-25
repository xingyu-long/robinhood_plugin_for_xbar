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


def show_total_change():
    portfolio = r.profiles.load_portfolio_profile()
    current_value = portfolio['equity']
    open_value = portfolio['equity_previous_close']

    change = float(current_value) - float(open_value)
    status = get_colored_status(change)
    print(f"{float(current_value):,.2f} {status}{abs(float(change)):,.2f}{DEFAULT_COLOR}")


def show_postions_as_list():
    # Use '---' to represent the list will show below.
    print("---")
    stock_info = "{:<10} {:<10} {:<10} {:<20}" + FONT + DEFAULT_COLOR
    print(stock_info.format("Symbol", "Equity", "Allocation", "Total"))
    my_stocks = r.account.build_holdings()
    for stock_name, values in sorted(my_stocks.items(),
                                     key=lambda kv: kv[1]["percentage"],
                                     reverse=True):
        total_change = float(values["percent_change"])
        status = get_colored_status(total_change)
        change_with_status = status + str(total_change) + "%"

        allocation = values["percentage"] + "%"
        print(stock_info.format(stock_name, values["equity"],
                                allocation, change_with_status))


def main():
    username = os.environ["ROBINHOOD_USERNAME"]
    password = os.environ["ROBINHOOD_PASSWORD"]
    r.login(username, password)
    show_total_change()
    show_postions_as_list()


if __name__ == '__main__':
    main()
