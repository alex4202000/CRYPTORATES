import cryptocompare

btc_inr = cryptocompare.get_price("BTC", currency="INR")
print(btc_inr)

doge_inr = cryptocompare.get_price("DOGE", currency="INR")
print(doge_inr)

ethereum_inr = cryptocompare.get_price("ETH", currency="INR")
print(ethereum_inr)

litecoin_inr = cryptocompare.get_price("LTC", currency="INR")
print(litecoin_inr)

Stellar_inr = cryptocompare.get_price("XLM", currency="INR")
print(Stellar_inr)



