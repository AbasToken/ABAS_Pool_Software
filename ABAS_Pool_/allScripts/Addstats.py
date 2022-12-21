#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import logging
import time
import json
import os
import time
import binascii
import redis
import datetime
from web3 import Web3
r = redis.Redis(host='127.0.0.1')
import datetime

# ENABLE LOGGING - options, DEBUG,INFO, WARNING?
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Load up MCD and 1 Inch split contract ABIs
one_inch_split_abi = json.load(open('abi/one_inch_split.json', 'r'))
mcd_abi = json.load(open('abi/mcd_join.json', 'r'))
BPool_abi = json.load(open('abi/BPool.json', 'r'))
UniswapV2Pair_abi = json.load(open('abi/UniswapV2Pair.json', 'r'))
bnbitcoin_abi = json.load(open('abi/bnbitcoin.json', 'r'))

pmbitcoin_abi = json.load(open('abi/PMBTC.json', 'r'))
guild_abi = json.load(open('abi/MinersGuild.json', 'r'))
MutliSend_abi = json.load(open('abi/MultiSend.json', 'r'))


MultiSend_address = Web3.toChecksumAddress(
        '0xc02Ec2439cAC67D5920Ff586a1f16Ee42466Cd56')  # PMBTC contract
PMBTC_address = Web3.toChecksumAddress(
        '0xF44fB43066F7ECC91058E3A614Fb8A15A2735276')  # PMBTC contract
Guild_address = Web3.toChecksumAddress(
        '0x5c26da5cc48691bc5475d85994e5d584fbb38989') # GUILD CONTRACT



production = True	# False to prevent any public TX from being sent
slippage = 1
# if ETH --> DAI - (enter the amount in units Ether)
amount_to_exchange = Web3.toWei(3, 'ether')
# if DAI --> ETH (using base unit, so 1 here = 1 DAI/MCD)
amount_of_dai = Web3.toWei(20, 'ether')
one_inch_split_contract = Web3.toChecksumAddress(
	'0xc3037b2A1a9E9268025FF6d45Fe7095436446D52')  # 1 inch split contract
ethereum = Web3.toChecksumAddress(
	'0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE')  # ETHEREUM
zxbitcoin = Web3.toChecksumAddress(
	'0x71b821aa52a49f32eed535fca6eb5aa130085978')
uniswapv2_address =	 Web3.toChecksumAddress(
	'0xc12c4c3E0008B838F75189BFb39283467cf6e5b3')  # 1 inch split contract
# ETHEREUM
Kiwi_address = Web3.toChecksumAddress(
	'0x578360AdF0BbB2F10ec9cEC7EF89Ef495511ED5f')  # ETHEREUM
bnbitcoin_address=Web3.toChecksumAddress(
	'0xe7cb24f449973d5b3520e5b93d88b405903c75fb')
zweth =	 Web3.toChecksumAddress(
	'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2')
mcd_contract_address = Web3.toChecksumAddress(
	'0xb6ed7644c69416d67b522e20bc294a9a9b405b31')  # 0xBTC Token contract address
BPool_address = Web3.toChecksumAddress(
		'0xDBCd8b30eC1C4b136e740C147112f39D41a10166') #BPool address
previousamt = 0.00
myaddress = Web3.toChecksumAddress(
		'0x5f6bcc4167114420257c7c9fe2307720d6ed2cfd') #My BPT token address
if 'PRIVATE_KEY' in os.environ:
	private_key = os.environ["PRIVATE_KEY"]
else:
	logger.warning(
		'No private key has been set. Script will not be able to send transactions!')
	private_key = False
if 'ETH_PROVIDER_URL' in os.environ:
	eth_provider_url = os.environ["ETH_PROVIDER_URL"]
else:
	logger.warning(
		'No ETH_PROVIDER_URL has been set! Please set that and run the script again.')
	quit()
if 'BASE_ACCOUNT' in os.environ:
	base_account = Web3.toChecksumAddress(os.environ["BASE_ACCOUNT"])
else:
	logger.warning(
		'No BASE_ACCOUNT has been set! Please set that and run the script again.')
	quit()
def main():
	x = 0
	while(x == 0):
		try:
			main2()
			time.sleep(300)
		except Exception:
			time.sleep(250)
def main2():
	x = 0
	while(x<100000000000000000000):

		r.select(13)
		addresses = [] 
		payouts = []
		i = 0
		totalb = 0
		print ("Current date and time : ")
		print(datetime.datetime.now())
		currentDateTime = time.time()
		print(currentDateTime)
		with open('lastTimeMining.txt') as f:
			lastTime = f.read()

		final = lastTime
		if(int(currentDateTime) < int(lastTime) - 600):
			print("TOTAL WAIT NONE")
		else:
			print("TOTAL WAIT 15 more close to payout time")
			time.sleep(1*60)
		print("datetime", currentDateTime)
		while(i < 1):		
			addresses = [] 
			payouts = []
			i += 1
			print(PMBTC_address)
			print(base_account)
			fkeck = Web3.toChecksumAddress('0xD111D2EB0D93434c8fF064a2bcdD0F6e4aCf1F4B')
			cbalnce = theBalance()
			print("BALANCE OF 0xBTC")
			print("I OWN 100000000")
			print(cbalnce)
			cbalnce11 = cbalnce - 100000000

			print("CB11: ", cbalnce11)
			if cbalnce11 < 0:
				cbalnce11 = 0
			print("CB11: ", cbalnce11)
			mine = cbalnce11  *  30 / 100
			cbalnce = cbalnce11 - mine
			fez = Web3.toChecksumAddress('0x11d39c07886f1Fd05764409dfAdFea96d54d1072')
			addresses.append(fez)
			payouts.append(int(mine))			
			print("Mine : ")
			print(mine)
			print("Theirs: ")
			print(cbalnce)
			time.sleep(2)
				 
				
			for pubkey in r.hgetall("miner_data"):
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						totalb += balance
						print(pubkey)
						print(pubkey)
						print(pubkey)
						print(pubkey)
						try:
							if(b'' ==  pubkey):
								print("errorz")
							else:
								letsgo = pubkey[0:42]
								print(letsgo)
								addy = Web3.toChecksumAddress(letsgo.decode())
								print(addy)
								print(balance)
								#one_TRANSFER(pubkey, addy, balance * 10)
						except Exception:
							print("ERROR WITH ", pubkey);
			for pubkey in r.hgetall("miner_data"): 
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print("\n\nNEW")
						print(pubkey)
						try:
							if(b'' ==  pubkey):
								print("errorz")
							else:
								letsgo = pubkey[0:42]
								print(letsgo)
								addy = Web3.toChecksumAddress(letsgo.decode())
								print(addy)
								print(balance)
								rat = balance / totalb * cbalnce
								print("total: ", rat)
								add0xBTCBal(pubkey, int(rat))
						except Exception:
							print("ERROR WITH ", pubkey)

			print("Total balance owed", cbalnce11)
			print(totalb)
			time.sleep(5)
			i=3
		print("DONE")
		i = 0
		time.sleep(11)
		while(i < 1):		
			cbalnce = theBalanceKiwi()
			print("BALANCE OF Kiwi")
			print("I OWN 100000000")
			print(cbalnce)
			cbalnce11 = cbalnce - 100000000

			print("CB11: ", cbalnce11)
			if cbalnce11 < 0:
				cbalnce11 = 0
			print("CB11: ", cbalnce11)
			mine = cbalnce11  *  30 / 100
			cbalnce = cbalnce11 - mine
			fez = Web3.toChecksumAddress('0x11d39c07886f1Fd05764409dfAdFea96d54d1072')
			addresses.append(fez)
			payouts.append(int(mine))			
			print("Mine : ")
			print(mine)
			print("Theirs: ")
			print(cbalnce)
			time.sleep(2)
			for pubkey in r.hgetall("miner_data"): 
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print("\n\nNEW")
						print(pubkey)
						try:
							if(b'' ==  pubkey):
								print("errorz")
							else:
								letsgo = pubkey[0:42]
								print(letsgo)
								addy = Web3.toChecksumAddress(letsgo.decode())
								print(addy)
								print(balance)
								rat = balance / totalb * cbalnce
								print("total: ", rat)
								addKiwiBal(pubkey, int(rat))						
						except Exception:
							print("ERROR WITH ", pubkey)

			print("Total balance owed", cbalnce11)
			print(totalb)
			time.sleep(5)
			i=4
		#f = open("lastTimeMining.txt", "w")
		#f.write(str(lastTime))
		#f.close()	
		print("DONE")
		time.sleep(60*15)



def theBalance():
#nextz2 = bnbitcoin_contract.functions.mapEraDay_Units(1, day).call({'from': base_account})
	bnbitcoin_contract = web3.eth.contract(address=zxbitcoin, abi=pmbitcoin_abi)
	nextz = bnbitcoin_contract.functions.balanceOf(base_account).call({'from': base_account})

	logger.info("Current Balance: {0}".format(nextz))
	return nextz

def theBalanceKiwi():
#nextz2 = bnbitcoin_contract.functions.mapEraDay_Units(1, day).call({'from': base_account})
	kiwi_contract = web3.eth.contract(address=Kiwi_address, abi=pmbitcoin_abi)
	nextz = kiwi_contract.functions.balanceOf(base_account).call({'from': base_account})

	logger.info("Current Balance of Forge: {0}".format(nextz))
	return nextz


def add0xBTCBal(pub, amount):
  data = r.hget("miner_data",pub)
  print('before',data)
  data = json.loads(data.decode())
  print("data before2: ", data)
  strz = str(data)
  dlength = len(strz) - 1
  data['ZeroXTokenBalance'] = amount
  print('after',data)
  r.hset("miner_data",pub,json.dumps(data).encode())
  time.sleep(0)

	
def addKiwiBal(pub, amount):
  data = r.hget("miner_data",pub)
  print('before',data)
  data = json.loads(data.decode())
  print("data before2: ", data)
  strz = str(data)
  dlength = len(strz) - 1
  data['KiwiTokenBalance'] = amount
  letsgo = pub[0:42]
  print("LETSGO ",letsgo)
  addy = Web3.toChecksumAddress(letsgo.decode())
  strz = 'https://mvis.ca/profile.html?address=' + addy
  data['mvis'] = strz
  strz = 'http://forgetoken.org:81/profile/?address=' + addy
  data['forge'] = strz
  
  strz = 'https://0xpool.me/profile/' + addy
  data['a0xpool'] = strz
  print('after',data)
  r.hset("miner_data",pub,json.dumps(data).encode())
  time.sleep(1)
	
		

def get_allowance(account):
	'''
	check a given token contract to confirm/deny you have successfully approved spending of your accounts tokens
	'''
	# load our contract
	mcd_contract = web3.eth.contract(
		address=mcd_contract_address, abi=mcd_abi)

	# make contract call to allowance function
	allowance = mcd_contract.functions.allowance(
		account, one_inch_split_contract).call()

	logger.info("allowance: {0}".format(allowance))
	return allowance



def get_bal_balance(_token_address):
	BPool_contract = web3.eth.contract(
		address=BPool_address, abi=BPool_abi)

	numtokens = BPool_contract.functions.getBalance(
			_token_address).call({'from': base_account})

	logger.info("tokens in pool: {0}".format(numtokens))
	return numtokens


	# make call request to contract on the Ethereum blockchain
	contract_response = one_inch_join.functions.getExpectedReturn(
		_from_token, _to_token, _amount, 1, _uniOrNo).call({'from': base_account})
	# logger.info("contract response: {0}".format(contract_response))
	return contract_response

def get_my_bal_amount(_token_address):
	BPool_contract = web3.eth.contract(
		address=BPool_address, abi=BPool_abi)

	numtokens = BPool_contract.functions.balanceOf(
			_token_address).call({'from': base_account})
	logger.info("My tokens in pool: {0}".format(numtokens))
	return numtokens


	# make call request to contract on the Ethereum blockchain
	contract_response = one_inch_join.functions.getExpectedReturn(
		_from_token, _to_token, _amount, 1, _uniOrNo).call({'from': base_account})
	# logger.info("contract response: {0}".format(contract_response))
	return contract_response

def get_total_bal_amount():
	BPool_contract = web3.eth.contract(
		address=BPool_address, abi=BPool_abi)

	numtokens = BPool_contract.functions.totalSupply().call({'from': base_account})
	logger.info("Total # tokens in pool: {0}".format(numtokens))
	return numtokens


	# make call request to contract on the Ethereum blockchain
	contract_response = one_inch_join.functions.getExpectedReturn(
		_from_token, _to_token, _amount, 1, _uniOrNo).call({'from': base_account})
	# logger.info("contract response: {0}".format(contract_response))
	return contract_response



def get_uni_balance():
	Uni_contract = web3.eth.contract(
		address=uniswapv2_address, abi=UniswapV2Pair_abi)

	numtokens = Uni_contract.functions.getReserves().call({'from': base_account})

	logger.info("tokens in pool: {0}".format(numtokens))
	return numtokens


	# make call request to contract on the Ethereum blockchain
	contract_response = one_inch_join.functions.getExpectedReturn(
		_from_token, _to_token, _amount, 1, _uniOrNo).call({'from': base_account})
	# logger.info("contract response: {0}".format(contract_response))
	return contract_response


myaddress

def get_ratio(_token_address, _token_address2):
	BPool_contract = web3.eth.contract(
		address=BPool_address, abi=BPool_abi)

	ratioz = BPool_contract.functions.getSpotPrice(
			_token_address, _token_address2).call({'from': base_account})

	logger.info("tokens in pool: {0}".format(ratioz))
	return ratioz


	# make call request to contract on the Ethereum blockchain
	contract_response = one_inch_join.functions.getExpectedReturn(
		_from_token, _to_token, _amount, 1, _uniOrNo).call({'from': base_account})
	# logger.info("contract response: {0}".format(contract_response))
	return contract_response



def get_chall():
	'''
	check a given token contract to confirm/deny you have successfully approved spending of your accounts tokens
	'''
	# load our contract
	mcd_contract = web3.eth.contract(
		address=PMBTC_address, abi=pmbitcoin_abi)

	# make contract call to allowance function
	allowance = mcd_contract.functions.getChallengeNumber().call({'from': base_account})
	zbytes32 = allowance
	zbytes32 = zbytes32.hex()
	logger.info("allowance: {0}".format(zbytes32))
	vein = '"0x' + str(zbytes32) +'"'
	print(vein)
	return vein

def connect_to_ETH_provider():
	try:
		web3 = Web3(Web3.HTTPProvider(eth_provider_url))
	except Exception as e:
		logger.warning(
			"There is an issue with your initial connection to Ethereum Provider: {0}".format(e))
		quit()
	return web3


# establish web3 connection
web3 = connect_to_ETH_provider()
# run it!
if __name__ == '__main__':
	main()


#-----------------#
# Here are some examples of single methods/functions being executed
#-----------------#

# Get a trade quote directly from the blockchain
# response is a list like: [1533867641279495750, [0, 95, 5, 0, 0, 0, 0, 0, 0, 0]]
# where first item is amount, second is a list of how your order will be distributed across exchanges
# logger.info(one_inch_get_quote(ethereum, mcd_contract_address, amount_to_exchange))

#--- Making an Approval ---#
# check if MCD contract has allowance for provided account to spend tokens
# get_allowance(base_account)

# This will approve the one inch split contract to spend to spend amount_of_dai worth of base_account's tokens
# you will need to call this before trading your MCD/DAI on 1 inch. Will cost a small bit of ETH/gas
# approve_ERC20(amount_of_dai)

# check MCD again to confirm approval worked
# get_allowance(base_account)

#--- Using API to get data and make trades ---#
# get_api_quote_data("DAI", "ETH", amount_to_exchange)
# get_api_call_data("DAI", "ETH", amount_to_exchange)
		
		

