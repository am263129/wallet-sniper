#!/usr/bin/env python3
from cProfile import run
import requests
import json
import blocksmith
import secrets
import time

running = True
while True:
  running = not running
  print(running)
  addresses = []
  privateKeys = []
  for i  in range(20):
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    if(len(private_key) == 64):
      address = blocksmith.EthereumWallet.generate_address(private_key)
      addresses.append(address)
      privateKeys.append(private_key)
  target = ""
  for address in addresses:
    target +=address+","
  x = requests.get(f'https://api.bscscan.com/api?module=account&action=balancemulti&address={target[:-1]}&tag=latest&apikey=key')
  y = requests.get(f'https://api.etherscan.io/api?module=account&action=balancemulti&address={target[:-1]}&tag=latest&apikey=key')
  z = requests.get(f'https://api.polygonscan.com/api?module=account&action=balancemulti&address={target[:-1]}&tag=latest&apikey=key')
  bsc_result = json.loads(x.text)
  eth_result = json.loads(y.text)
  polygon_result = json.loads(z.text)
  for i in range(len(bsc_result['result'])):
    if int(bsc_result["result"][i]["balance"]) > 0 or int(eth_result["result"][i]["balance"]) > 0 or int(polygon_result["result"][i]["balance"]) > 0:
      print(privateKeys[i])
      print(addresses[i])
      input_dictionary = {"key" : privateKeys[i], "address" : addresses[i], "bsc_balance":bsc_result["result"][i]["balance"], "eth_balance":eth_result["result"][i]["balance"], "polygon_balance":polygon_result["result"][i]["balance"]}
      file = open("result.txt", "a")
      str = repr(input_dictionary)
      file.write("goal! = " + str + "\n")
      file.close()
  time.sleep(0.1)
