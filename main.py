import requests
import re
import ghasedakpack
from bs4 import BeautifulSoup


site_address = 'https://arzdigital.com/coins/bitcoin/'
get_site_address = requests.get(site_address)
soup_site = BeautifulSoup(get_site_address.text, 'html.parser')
bitcoin_price_result = soup_site.find('div', attrs={'class': 'arz-coin-page-data__coin-price coinPrice btcprice pulser'})
tether_price_result = soup_site.find('span', attrs={'class': 'arz-tether-price'})

re_text = re.sub(r'[^\w]', ' ', bitcoin_price_result.text)
re_text = re_text.strip()
bitcoin_price = re_text.replace(" ", "")

tether_price_result = tether_price_result.text
tether_price_result = tether_price_result.replace(",", "")

final_bitcoin_price = int(bitcoin_price) * int(tether_price_result)
info_for_user = "Today bitcoin price in Tomans :> " + str(final_bitcoin_price)

print(info_for_user)
print(int(tether_price_result))

sms = ghasedakpack.Ghasedak("Your API Key in ghasedak.me")
sms.send({'message': info_for_user, 'receptor' : 'Your registered phone in ghasedak.me', 'linenumber': 'Your line number in ghasedak.me'})