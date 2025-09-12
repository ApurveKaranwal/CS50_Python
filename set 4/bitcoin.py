'''In a file called bitcoin.py, implement a program that:
Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛,
 that they would like to buy. If that argument cannot be converted to a float, 
 the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin
 Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey.
  You should replace YourApiKey with the actual API key you obtained
   from your CoinCap account dashboard, which returns a JSON object, among whose nested 
keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.'''

import requests

try:
    ...
except requests.RequestException:
    ...