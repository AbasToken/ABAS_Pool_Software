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

r.select(13)
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


KIWI_address = Web3.toChecksumAddress(
        '0x7cb16cb78ea464ad35c8a50abf95dff3c9e09d5d')  # PMBTC contract
MultiSend_address = Web3.toChecksumAddress(
        '0xD3d9c1b979D24604eCB595Df76065b4b76489D32')  # PMBTC contract
PMBTC_address = Web3.toChecksumAddress(
        '0x027e2eB1C79bD1921a29fd377A8C978B3193401c')  # PMBTC contract
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
	'0x11f38b2aff86ff9f253f6fd91378e4c7dadf5667')
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
		print ("Current date and time FIX THE SCRIPT TO NOT HAVE NO REDUCTION IN REWARDS : ")
		v = web3.eth.gasPrice
		print ("Current date and time : ", v)
		print(datetime.datetime.now())
		currentDateTime = time.time()
		print(currentDateTime)
		with open('lastTimeMining.txt') as f:
			lastTime = f.read()
		print("lasttime", lastTime)
		if(int(lastTime)>currentDateTime):
			winner = int(lastTime)
		else:
			winner = currentDateTime
		
		print("winner", lastTime)
		print("winner2", int(lastTime))
		final = int(winner) - int(currentDateTime)
		print("TOTAL WAIT", final)
		print("datetime", currentDateTime)
		lastTime = int(currentDateTime) + 60*60*24*3 + final + int(3*60)
		print("winnelastTimer", lastTime)
		print("FINALLLL : ", final)
		if(final>0):		
			time.sleep(final)
		print("winnelastTimer", lastTime)
		print("winnelastTimer", lastTime)
		while(i < 1):	
			print("Start of payouts, 0xbtc first")
			addresses = [] 
			payouts = []
			i += 1
			totalb = 0
			print(PMBTC_address)
			print(base_account)
			fkeck = Web3.toChecksumAddress('0xD111D2EB0D93434c8fF064a2bcdD0F6e4aCf1F4B')
			cbalnce = theBalance()
			print("BALANCE OF 0xbtc")
			print("I OWN 100000000")
			print(cbalnce)
			cbalnce11 = cbalnce - 100000000
			if(cbalnce11 < 1000000):
				break
			print("CB11: ", cbalnce11)
			if cbalnce11 < 0:
				cbalnce11 = 0
			print("CB11: ", cbalnce11)
			mine = cbalnce11  * 30 / 100
			cbalnce = cbalnce11 - mine
			fez = Web3.toChecksumAddress('0x11d39c07886f1Fd05764409dfAdFea96d54d1072')		
			print("Mine : ")
			print(mine)
			print("Theirs: ")
			print(cbalnce) 
			for pubkey in r.hgetall("miner_data"):
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						try:
							totalb += balance
							print(pubkey)
							letsgo = pubkey[0:42]
							print(letsgo)
							addy = Web3.toChecksumAddress(letsgo.decode())
							print(addy)
							print(balance)
							#one_TRANSFER(pubkey, addy, balance * 10)
						except Exception:
							print("ERROR WITH ", pubkey);
							time.sleep(15)
			for pubkey in r.hgetall("miner_data"): 
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print("\n\nNEW")
						print(pubkey)
						try:
							letsgo = pubkey[0:42]
							print(letsgo)
							addy = Web3.toChecksumAddress(letsgo.decode())
							if(addy == "0x11d39c07886f1Fd05764409dfAdFea96d54d1072"):
								print("bananas")
								addy = "0xc7D93A4Fcc075B2C3DEB1FC9606198152aCaAA04"
								time.sleep(1)
							print(addy)
							print(balance)
							rat = balance / totalb * cbalnce
							print("total: ", rat)				
							add0xBTCBal(pubkey,int(rat))				
							if(addy in addresses):
								try:
									place = addresses.index(addy)
									oldbal = payouts[place]
									print("multi workers adding balance ", oldbal, " to this ",rat)
									payouts[place] = int(oldbal) + int(rat)
								except:
									"issue!"
							else:
								addresses.append(addy)
								payouts.append(int(rat))
							
						except Exception:
							print("ERROR WITH ", pubkey);
							time.sleep(15)
						
			addresses.append(fez)
			payouts.append(int(mine))	
			print(addresses)
			print(payouts)

			print("Total balance owed 0xbtc", cbalnce11)
			print(totalb)
			try:	
				print(totalb)
				if cbalnce11 > 1:
					fff = 5
				test = one_MATIC(addresses, payouts, int(cbalnce11))
				if(test == False):
					i=0
			except Exception:
				print("EXCEPTION")
				print(miner)
				i = 0
			time.sleep(65)
		print("DONE w 0xBTC")
		i=0
		while(i < 1):	

			print("Start of Kiwi")
			addresses = [] 
			payouts = []
			i += 1
			totalb = 0
			print(PMBTC_address)
			print(base_account)
			fkeck = Web3.toChecksumAddress('0xD111D2EB0D93434c8fF064a2bcdD0F6e4aCf1F4B')
			cbalnce = theBalanceKiwi()
			print("BALANCE OF KIWI")
			print("I OWN 100000000")
			print(cbalnce)
			cbalnce11 = cbalnce - 100000000
			if(cbalnce11 < 10000000):
				break
			print("CB11: ", cbalnce11)
			if cbalnce11 < 0:
				cbalnce11 = 0
			print("CB11: ", cbalnce11)
			mine = cbalnce11 * 30 / 100
			cbalnce = cbalnce11 - mine
			fez = Web3.toChecksumAddress('0x11d39c07886f1Fd05764409dfAdFea96d54d1072')		
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
						try:
							totalb += balance
							print(pubkey)
							letsgo = pubkey[0:42]
							print(letsgo)
							addy = Web3.toChecksumAddress(letsgo.decode())
							print(addy)
							print(balance)
							#one_TRANSFER(pubkey, addy, balance * 10)
							
						except Exception:
							print("ERROR WITH ", pubkey);
							time.sleep(15)
			for pubkey in r.hgetall("miner_data"): 
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print("\n\nNEW")
						print(pubkey)
						try:
							letsgo = pubkey[0:42]
							print(letsgo)
							addy = Web3.toChecksumAddress(letsgo.decode())
							if(addy == "0x11d39c07886f1Fd05764409dfAdFea96d54d1072"):
								print("bananas")
								addy = "0xc7D93A4Fcc075B2C3DEB1FC9606198152aCaAA04"
								time.sleep(1)
							print(addy)
							print(balance)
							rat = balance / totalb * cbalnce
							print("total: ", rat)			
							addKiwiBal(pubkey,int(rat))			
							if(addy in addresses):
								try:
									place = addresses.index(addy)
									oldbal = payouts[place]
									print("multi workers adding balance ", oldbal, " to this ",rat)
									payouts[place] = int(oldbal) + int(rat)
								except:
									"issue!"
							else:
								addresses.append(addy)
								payouts.append(int(rat))
								
						except Exception:
							print("ERROR WITH ", pubkey);
							time.sleep(15)
						

			addresses.append(fez)
			payouts.append(int(mine))			
			print(addresses)
			print(payouts)

			print("Total Kiwi owed", cbalnce11)
			print(totalb)
			try:	
				print(totalb)
				if cbalnce11 > 1:
					fff = 5
				test = one_KIWI(addresses, payouts, int(cbalnce11))
				if(test == False):
					i = 0
			except Exception:
				print("EXCEPTION")
				print(miner)
				i = 0
			time.sleep(65)
		print("DONE with Kiwi")

		i = 0
		test = 3223333
		saved = theBalance2()
		while(i < 1):	
			fez = Web3.toChecksumAddress('0x96C14F84981A67482201CFc4a1D1D804F81e4be6')
			print("Start of Forge")
			addresses = []
			payouts = []	
			totaler = 0
			i += 1
			r.set("reloadAccountBalance", 2)
		
			print(PMBTC_address)
			time.sleep(1)
			for pubkey in r.hgetall("miner_data"):
				#try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print(pubkey)
						try:
							letsgo = pubkey[0:42]
							print(letsgo)
							addy = Web3.toChecksumAddress(letsgo.decode())
							if(addy == "0x11d39c07886f1Fd05764409dfAdFea96d54d1072"):
								print("bananas")
								addy = "0x96C14F84981A67482201CFc4a1D1D804F81e4be6"
								time.sleep(1)					
							if(addy in addresses):
								try:
									place = addresses.index(addy)
									oldbal = payouts[place]
									print("multi workers adding balance ", oldbal, " to this ",balance)
									payouts[place] = oldbal + balance*10**10
									totaler = totaler + balance*10**10
								except:
									"issue!"
							else:
								print("balance START", addy, " to this ",balance)
								addresses.append(addy)
								payouts.append(balance*10**10)
								totaler = totaler + balance*10**10
							
						except Exception:
							print("ERROR WITH ", pubkey);
							time.sleep(15)
			print("NEWNEW")
			print(payouts)
			print(addresses)
			print("TOTAL FORGE: ", totaler/(10**18))
			poolzforge = totaler *  45 / 105
			print("Pools FORGE: ", poolzforge )
			fkeck = Web3.toChecksumAddress('0x96C14F84981A67482201CFc4a1D1D804F81e4be6')
			#print("Sending: ", str(totaler/4.4), " to ", fez)
			#if(totaler == 0):
			#	break
			addresses.append(fkeck)
			payouts.append(int(poolzforge))	
			print("NEWNEW Forge Payout Scheme")
			print(payouts)
			print(addresses)
			saved23 = theBalance2()			
			print("saved: ", saved, " >  is greather than this to exit  saved23: ", saved23)
			if(saved > saved23):
				print("exiting RIGHT NOW")
				break
			#try:
			vest = one_inch_token_swap(addresses, payouts)
			time.sleep(55)
			saved2 = theBalance2()
			print("saved: ", saved, " vs EQUALS : ", saved2)
			if(not vest and saved <= saved2):
				print("GO AGAIN")
				i = 0
			else:
				print("SUCCESS lets get this miner online again")
		#except Exception:
			print("EXCEPTION")
			i = 0
			time.sleep(65)
		f = open("lastTimeMining.txt", "w")
		f.write(str(lastTime))
		f.close()	
		print("DONE FORGE AND ALL")
		time.sleep(6)



def theBalance():
#nextz2 = bnbitcoin_contract.functions.mapEraDay_Units(1, day).call({'from': base_account})
	bnbitcoin_contract = web3.eth.contract(address=zxbitcoin, abi=pmbitcoin_abi)
	nextz = bnbitcoin_contract.functions.balanceOf(base_account).call({'from': base_account})

	logger.info("Current Balance: {0}".format(nextz))
	return nextz

def theBalance2():
#nextz2 = bnbitcoin_contract.functions.mapEraDay_Units(1, day).call({'from': base_account})
	bnbitcoin_contract = web3.eth.contract(address=PMBTC_address, abi=pmbitcoin_abi)
	nextz = bnbitcoin_contract.functions.balanceOf(base_account).call({'from': base_account})

	logger.info("Current Balance of Forge: {0}".format(nextz))
	return nextz

def theBalanceKiwi():
#nextz2 = bnbitcoin_contract.functions.mapEraDay_Units(1, day).call({'from': base_account})
	kiwi_contract = web3.eth.contract(address=KIWI_address, abi=pmbitcoin_abi)
	nextz = kiwi_contract.functions.balanceOf(base_account).call({'from': base_account})

	logger.info("Current Balance of Forge: {0}".format(nextz))
	return nextz

def decrement(pub, amount):
  data = r.hget("miner_data",pub)
  print('before',data)
  data = json.loads(data.decode())
  data['tokenBalance'] -= amount
  data['tokensAwarded'] += amount
	
  try:
  	bal = data['ZeroXTokenBalance']
  except Exception:
  	bal = 0

  #print(" Zero X BALANCE: ", bal)
  data['ZeroXTokenBalance'] = 0


  try:
  	data['ZeroXTokenAwarded'] += bal
  except Exception:
  	data['ZeroXTokenAwarded'] = bal
  print('ZeroXTokenAwarded : ', data['ZeroXTokenAwarded'])

  try:
  	bal2 = data['KiwiTokenBalance']
  except Exception:
  	bal2 = 0
  #print(" KIWI BALANCE: ", bal2)

  data['KiwiTokenBalance'] = 0

  try:
  	data['KiwiTokenAwarded'] += bal2
  except Exception:
  	data['KiwiTokenAwarded'] = bal2
 # print('KiwiTokenAwarded : ', data['KiwiTokenAwarded'])	


  r.hset("miner_data",pub,json.dumps(data).encode())
#  print('after DECREMENT data',data)
#deletes shares after distribution
 # addy = pub.decode()
 # f = 'miner_submitted_share:'+str(addy)
 # test = r.ltrim(f, 1, 0)


def add0xBTCBal(pub, amount):
  data = r.hget("miner_data",pub)
 # print('before',data)
  data = json.loads(data.decode())
 # print("data before2: ", data)
  strz = str(data)
  dlength = len(strz) - 1
  data['ZeroXTokenBalance'] = amount
#  print('after',data)
  r.hset("miner_data",pub,json.dumps(data).encode())
  
  time.sleep(0)

	
def addKiwiBal(pub, amount):
  data = r.hget("miner_data",pub)
#  print('before',data)
  data = json.loads(data.decode())
#  print("data before2: ", data)
  strz = str(data)
  dlength = len(strz) - 1
  data['KiwiTokenBalance'] = amount
#  print('after',data)
  r.hset("miner_data",pub,json.dumps(data).encode())
  time.sleep(1)
	
	

def one_inch_token_swap(addresses, balances):
	print("BOOBIE")
	print(type(addresses))
	print([type(k) for k in addresses])
	print(type(balances))
	print([type(k) for k in balances])
	saved = theBalance2()
	# get quote for trade,
	print(balances)
	print(addresses)
	MultiSend_send = web3.eth.contract(address=MultiSend_address, abi=MutliSend_abi)
	
	data = MultiSend_send.encodeABI(fn_name="multiSend", args=[PMBTC_address, addresses, balances])
	gaz = 100000000
	# get our nonce
	nonce = web3.eth.getTransactionCount(base_account)
	tx = {
		'chainId': web3.toHex(42161),
		'nonce': nonce,
		'to': MultiSend_address,
		'value': 0,
		'gasPrice': gaz,
		'from': base_account,
		'data': data
	}

	# get gas estimate
	gas = web3.eth.estimateGas(tx)*2
	logger.info("GAS: {0}".format(gas))
	tx["gas"] = gas

	logger.info('transaction data: {0}'.format(tx))

	# sign and broadcast our trade
	if private_key and production == True:
		try:
			print('hehe')
			signed_tx = web3.eth.account.signTransaction(tx, private_key)
		except:
			logger.exception("Failed to created signed TX!")
			return False
		try:
			tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			logger.info("TXID: {0}".format(web3.toHex(tx_hash)))
			sourceFile = open('demo.txt', 'a')
			print('FORGE TRANSACTION TX IS {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			print(addresses, file = sourceFile)
			print(balances, file = sourceFile)
			print('FORGE TRANSACTION TX IS {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			sourceFile.close()
			time.sleep(112)
			txReceipt = web3.eth.getTransactionReceipt(tx_hash)
			print("yes?", txReceipt)
			if (txReceipt and txReceipt.blockNumber):
				print("yesYESYESYESYESYESYESYSE")
			else:
				print("nonononoNONONONONONONO")
			for pubkey in r.hgetall("miner_data"):
				try:
					miner = r.hget("miner_data", pubkey)
					minerData = json.loads(miner.decode())
					balance = int(minerData['tokenBalance'])
					if balance > 0:
						print(pubkey)
						decrement(pubkey, balance)
				except Exception as e:
					print("error: ", e)
					print("Fail ", pubkey)
			SKIPREDUCTION = 0
			r.set('challengeNumber', get_chall())
			v = r.delete('queued_transactions')
			v = r.delete('queued_transactions')
			v = r.delete('queuedTxCount')
			v = r.delete('pendingMintsCount')
			v = r.delete('lost_transactions_list')
			v = r.delete('unconfirmed_submitted_solution_tx')
			v2 = r.delete('lastChallengesubmit2')
			v = r.delete('lastChallengesubmit')
		except:
			logger.warning("Failed sending TX to 1 inch!")
			return False
	else:
		logger.info('No private key found! Transaction has not been broadcast!')
	return True



def one_MATIC(addresses, balances, totalz):
	print(type(addresses))
	print([type(k) for k in addresses])
	print(type(balances))
	print([type(k) for k in balances])
	# get quote for trade,
	
	MultiSend_send = web3.eth.contract(address=MultiSend_address, abi=MutliSend_abi)
	
	data = MultiSend_send.encodeABI(fn_name="multiSend", args=[zxbitcoin, addresses, balances])
	gaz = web3.eth.gasPrice * 2	
	while(gaz >  152900000000):	
		print("WAITING FOR LOWER GAS TO SEND PAYMENTS")
		time.sleep(30)
		gaz = web3.eth.gasPrice * 2
	# get our nonce
	nonce = web3.eth.getTransactionCount(base_account)
	tx = {
		'chainId': web3.toHex(42161),
		'nonce': nonce,
		'to': MultiSend_address,
		'value': 0,
		'gasPrice': gaz,
		'from': base_account,
		'data': data
	}

	# get gas estimate
	gas = web3.eth.estimateGas(tx)
	logger.info("GAS: {0}".format(gas))
	tx["gas"] = gas

	logger.info('transaction data: {0}'.format(tx))

	# sign and broadcast our trade
	if private_key and production == True:
		try:
			signed_tx = web3.eth.account.signTransaction(tx, private_key)
		except:
			logger.exception("Failed to created signed TX!")
			return False
		try:
			tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			logger.info("TXID: {0}".format(web3.toHex(tx_hash)))
			sourceFile = open('demo.txt', 'a')
			print(' ZERO x BTC 0xBTC TRANSACTION TX IS  {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			print(addresses, file = sourceFile)
			print(balances, file = sourceFile)
			print(' ZERO x BTC 0xBTC TRANSACTION TX IS  {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			sourceFile.close()
			time.sleep(5)

		except:
			logger.warning("Failed sending TX to 1 inch!")
			return False
	else:
		logger.info('No private key found! Transaction has not been broadcast!')
	return True

def one_KIWI(addresses, balances, totalz):
	print(type(addresses))
	print([type(k) for k in addresses])
	print(type(balances))
	print([type(k) for k in balances])
	# get quote for trade,
	
	MultiSend_send = web3.eth.contract(address=MultiSend_address, abi=MutliSend_abi)
	
	data = MultiSend_send.encodeABI(fn_name="multiSend", args=[KIWI_address, addresses, balances])
	gaz = web3.eth.gasPrice * 2
	while(gaz >  152900000000):
		print("WAITING FOR LOWER GAS TO SEND PAYMENTS")
		time.sleep(30)
		gaz = web3.eth.gasPrice * 2
	# get our nonce
	nonce = web3.eth.getTransactionCount(base_account)
	tx = {
		'chainId': web3.toHex(42161),
		'nonce': nonce,
		'to': MultiSend_address,
		'value': 0,
		'gasPrice': gaz,
		'from': base_account,
		'data': data
	}

	# get gas estimate
	gas = web3.eth.estimateGas(tx)
	logger.info("GAS: {0}".format(gas))
	tx["gas"] = gas

	logger.info('transaction data: {0}'.format(tx))

	# sign and broadcast our trade
	if private_key and production == True:
		try:
			signed_tx = web3.eth.account.signTransaction(tx, private_key)
		except:
			logger.exception("Failed to created signed TX!")
			return False
		try:
			tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			logger.info("TXID: {0}".format(web3.toHex(tx_hash)))
			sourceFile = open('demo.txt', 'a')
			print('KIWI TRANSACTION TX IS  {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			print(addresses, file = sourceFile)
			print(balances, file = sourceFile)
			print('KIWI TRANSACTION TX IS  {0}'.format(web3.toHex(tx_hash)), file = sourceFile)
			sourceFile.close()
			time.sleep(5)

		except:
			logger.warning("Failed sending TX to 1 inch!")
			return False
	else:
		logger.info('No private key found! Transaction has not been broadcast!')
	return True


def approve_ERC20(_amount_of_ERC):
	'''
	Send a transaction to MCD/DAI contract approving 1 Inch join contract to spend _amount_of_ERC worth of base_accounts tokens
	'''
	# load our contract
	mcd_contract = web3.eth.contract(
		address=mcd_contract_address, abi=mcd_abi)

	allowance_before = get_allowance(base_account)
	logger.info("allowance before: {0}".format(allowance_before))

	# get our nonce
	nonce = web3.eth.getTransactionCount(base_account)

	# encode our data
	data = mcd_contract.encodeABI(fn_name="approve", args=[
		one_inch_split_contract, _amount_of_ERC])

	tx = {
		'nonce': nonce,
		'to': mcd_contract_address,
		'value': 0,
		'gasPrice': web3.eth.gasPrice,
		'from': base_account,
		'data': data
	}

	# get gas estimate
	tx["gas"] = web3.eth.estimateGas(tx)

	logger.info('transaction data: {0}'.format(tx))

	# sign and broadcast our trade
	if private_key and production == True:
		try:
			signed_tx = web3.eth.account.signTransaction(tx, private_key)
		except:
			logger.exception("Failed to created signed TX!")
			return False
		try:
			tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
			logger.info("TXID from 1 Inch: {0}".format(web3.toHex(tx_hash)))
		except:
			logger.warning("Failed sending TX to 1 inch!")
			return False
	else:
		logger.info('No private key found! Transaction has not been broadcast!')
		
		

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
		
		

