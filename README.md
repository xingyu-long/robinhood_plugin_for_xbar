# Robinhood plugin for xbar
This plugin provides the easiest way to access your portfolio value and held positions.
![Example](screenshot/example.jpg)

## How to use it
* Download the latest release of [xbar](https://github.com/matryer/xbar#get-started).
* Install [robin-stocks](https://github.com/jmfernandes/robin_stocks) package.
  ```
  $ pip install robin_stocks
  ```
* Clone this repo and modify username and password
  ```
  $ git clone https://github.com/xingyu-long/robinhood_plugin_for_xbar.git
  $ chmod 755 robinhood.1m.py # In case xbar cannot run it.
  ```

## Troubleshooting
* login issue
  ```
  exit status 1: Traceback (most recent call last):
  File "/Users/clarklong/Library/Application Support/xbar/plugins/./robinhood. 1m.py", line 75, in <module>
  main()
  File "/Users/clarklong/Library/Application Support/xbar/plugins/./robinhood. 1m.py", line 69, in main
  r.login (username, password)
  File /usr/local/lib/python3.9/site-packages/robin_stocks/robinhood/authentication.py", line 168, in login
  sms code = input('Enter Robinhood code for validation: ")
  EOFError: EOF when reading a line
  ```
  Solution: You can run this script with your terminal first and fill the verification code. But it should be fixed later
  with proper prompt. 
