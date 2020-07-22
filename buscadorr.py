!pip install pywallet
from pywallet import wallet
import time
import requests
while True:
  time.sleep(1)
  seed = wallet.generate_mnemonic()
  random_wallet = wallet.create_wallet(network="BTC", seed=seed, children=1)
  resp = requests.get('https://blockchain.info/balance?active=' + random_wallet['address'])
  minerstat = resp.json()
  print(minerstat,'      ',random_wallet)
