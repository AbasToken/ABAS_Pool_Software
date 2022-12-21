# ABAS_Pool_Software
Pool Software to run your own pool for ABAS, for Ubuntu
Token Contract: 0x027e2eB1C79bD1921a29fd377A8C978B3193401c


To add Delay inbetweeen sending transactions, reference /lib/transaction-cordinator.js line 77
Default Delay 5 minutes.

Install your Private Key and Address in account.config.js

Change from my Provider to Your Provider. (Search and replace all files)
My Provider URL: https://arb-mainnet.g.alchemy.com/v2/WHa04zxQ0-gU4lKeWM0Se47WOG8RZpg3
Replace this with yours

### Token Mining Pool  

Developed by the ABAS and 0xBitcoin Community

(GNU PUBLIC LICENSE)

A pool for mining RC20 Tokens

### BASIC SETUP  (needs Node8)
0. install Node8
1. npm install -g node-gyp
1. sudo apt-get install build-essential
2. npm install
3. npm run webpack  #(to build the website files)
4. input private key and address for pool into 'account.config.js'

5. install redis-server and make sure it is running(see below for instructions)
6. Edit pool.config.js to your tastes
7. Edit the website files in /public/  to change the look of the website
8. npm run server #(or npm run server test for Ropsten test net)
9. Open ports 16129, 11181, 13000, 12095 for outside viewing

### HOW TO USE
1. Point a poolminer at your pool using http://localhost:16129  (or ipaddress:16129 or domain.com:16129)  (make sure firewall allows this port)
2. View website interface at http://localhost:11181 (you can set up nginx to serve the static files in /public)


## Installing Redis  
  1. sudo apt-get install redis
  2. sudo service redis-server start

   - Redis will serve/connect at localhost:6379 by default - the pool will use this port

## Redis Commands

Must approve from your pool account ABAS on MultiSend contract @ for the payout contract
Go TO: 
https://arbiscan.io/token/0x027e2eB1C79bD1921a29fd377A8C978B3193401c#writeContract#F2

Enter:
spender: 0xD3d9c1b979D24604eCB595Df76065b4b76489D32
amount: 99999999999999999999999999999999999
