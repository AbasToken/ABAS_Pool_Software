


const Tx = require('ethereumjs-tx')

var tokenContractJSON = require('../app/assets/contracts/_BNbitcoinToken.json');
var mintHelperContractJSON = require('../app/assets/contracts/MintHelper.json');
var deployedContractInfo = require('../app/assets/contracts/DeployedContractInfo.json');
var web3Utils = require('web3-utils')
var cluster = require('cluster')


//var busySendingSolution = false;
//var queuedMiningSolutions = [];

//var queuedTokenTransfers = []; //keep trying if failed to mine or something
//var queuedTokenTransferCount = 0;
//var lastSubmittedMiningSolutionChallengeNumber;



//  var busySendingTransfer = false;


  var transactionCoordinator = require('./transaction-coordinator')

/**
BUG : pool is resending transactions!

**/




module.exports =  {


  async init(redisInterface, web3, accountConfig, poolConfig, pool_env )
  {

    this.redisInterface=redisInterface;
    this.web3=web3;
    this.pool_env = pool_env;
    this.poolConfig = poolConfig;
    this.accountConfig = accountConfig;
    this.tokenContract =  new web3.eth.Contract(tokenContractJSON.abi,this.getTokenContractAddress())
    this.mintHelperContract = new web3.eth.Contract(mintHelperContractJSON.abi, this.accountConfig.minting.helper)



    if (cluster.isMaster) {
      this.redisInterface.dropList("recent_challenges");
      // load up the list with 5 blank entries ... saves having to always check the size 
      // of the list later.
      this.redisInterface.pushToRedisList("recent_challenges", ["-", "-", "-", "-", "-"]);
    }


  //  this.difficultyTarget = 111;
    //this.challengeNumber = 1111;


  },

 async  update()
  {


      //reply ok
   transactionCoordinator.init(this.web3,this.tokenContract, this.mintHelperContract,this.poolConfig,this.accountConfig,this.redisInterface,this)


    var self=this;


    await self.collectTokenParameters();

     setInterval(function(){ self.collectTokenParameters()},2000*120);



  },




  async getPoolChallengeNumber()
  {
    return await this.redisInterface.loadRedisData('challengeNumber');
  },
  async getEpochCount()
  {
    return await this.redisInterface.loadRedisData('epochCount');
  },

  async getPoolDifficultyTarget()
  {
     var targetString = await this.redisInterface.loadRedisData('miningTarget');
     return  targetString
  },

  async getPoolDifficulty()
  {
    return await this.redisInterface.loadRedisData('miningDifficulty');
  },


  async collectTokenParameters( )
  {
    if (!cluster.isMaster) { return; }


    var miningDifficultyString = await this.tokenContract.methods.getMiningDifficulty().call()  ;
    var miningDifficulty = parseInt(miningDifficultyString)

    var miningTargetString = await this.tokenContract.methods.getMiningTarget().call()  ;
    var miningTarget = web3Utils.toBN(miningTargetString)

    var challengeNumber = await this.tokenContract.methods.getChallengeNumber().call() ;
    var epochCount = await this.tokenContract.methods.epochCount().call() ;




    // console.log('Mining difficulty:', miningDifficulty);
    // console.log('Mining target:', miningTargetString);
    if (challengeNumber != this.challengeNumber) {

      // check if we've seen this challenge before
      var seenBefore = await this.redisInterface.isElementInRedisList("recent_challenges", challengeNumber);
      if (!seenBefore) {
        this.challengeNumber = challengeNumber;
        console.log('New challenge:', challengeNumber);
        this.redisInterface.pushToRedisList("recent_challenges", challengeNumber);
        this.redisInterface.popLastFromRedisList("recent_challenges");
        this.redisInterface.storeRedisData('challengeNumber',challengeNumber)
        this.redisInterface.storeRedisData('epochCount',epochCount)
      } else {
        //console.log('Old challenge:', challengeNumber);
      }
	console.log("Epoch: ", epochCount);
    }



      this.miningDifficulty = miningDifficulty;
      this.difficultyTarget = miningTarget;

      this.redisInterface.storeRedisData('miningDifficulty',miningDifficulty)
      this.redisInterface.storeRedisData('miningTarget',   miningTarget.toString()  )

        console.log('New miningDifficulty:', miningDifficulty);

      var web3 = this.web3;
      var ethBlockNumber = await new Promise(function (fulfilled,error) {
            web3.eth.getBlockNumber(function(err, result)
          {
            if(err){error(err);return}
            //console.log('eth block number ', result )
            fulfilled(result);
            return;
          });
       });


      this.redisInterface.storeRedisData('ethBlockNumber', ethBlockNumber );


  },


  async getEthBlockNumber()
  {
    var result = parseInt( await this.redisInterface.loadRedisData('ethBlockNumber' ));

    if(isNaN(result) || result < 1) result = 0 ;

    return result
  },

  getTokenContractAddress()
  {
    if(this.pool_env == 'test')
    {
      return deployedContractInfo.networks.testnet.contracts._BNbitcointoken.blockchain_address;
    }else if(this.pool_env == 'staging'){
      return deployedContractInfo.networks.staging.contracts._bnbitcointoken.blockchain_address;
    }else{
      return deployedContractInfo.networks.mainnet.contracts._bnbitcointoken.blockchain_address;
    }

  },



//use address from ?
  async queueMiningSolution( solution_number,minerEthAddress,challenge_digest,challenge_number )
  {

    var currentTokenMiningReward = await this.requestCurrentTokenMiningReward()


      var txData= {
          minerEthAddress: minerEthAddress,    //we use this differently in the pool!
          solution_number: solution_number,
          challenge_digest: challenge_digest,
          challenge_number: challenge_number,
          tokenReward: currentTokenMiningReward
        }

        await transactionCoordinator.addTransactionToQueue('solution',txData)

  },

//minerEthAddress
  async queueTokenTransfer(addressTo, tokenAmount, balancePaymentId)
  {
    var txData= {

      addressTo:addressTo,
      tokenAmount:tokenAmount,
      balancePaymentId: balancePaymentId

    }


    //await transactionCoordinator.addTransactionToQueue('transfer',txData)


  },








   async requestCurrentTokenMiningReward()
   {


     var self = this ;
     var reward_amount =  new Promise(function (fulfilled,error) {

       self.tokenContract.methods.getMiningReward().call(function(err, result){
          if(err){error(err);return;}

          fulfilled(result)

        });
      });



     return reward_amount;
   },






}
