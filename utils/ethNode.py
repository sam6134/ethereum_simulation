from re import S
from web3 import Web3
import time

class ethNode:
    def __init__(self, ipcAddrPath: str):
        """
            `ipcAddrPath`: path to ipc endpoint of eth-chain
        """
        self.endPt =  Web3(Web3.IPCProvider(ipcAddrPath))
    
    def isConnected(self) -> bool:
        """
            `returns`: if node is connected
        """
        return self.endPt.isConnected()
    
    def getEnodeAddr(self) -> str:
        """
            `returns`: enode address
        """
        return self.endPt.geth.admin.node_info()['enode']
    

    def addPeer(self, enodeAddr: str):
        """
            `enodeAddr`: address of enode to be Added
            `returns`: None / raises exception in case of an error
        """
        try:
            self.endPt.geth.admin.add_peer(enodeAddr)
            print("Added peer {} Successfully".format(enodeAddr))
        except Exception as e:
            print(e)
            raise Exception("Error adding Node with address" + enodeAddr)
    
    def getMinerAccountAddr(self, passphrase="1234") -> str:
        """
            `passphrase` opt: for new miner account if None
            `returns`: the default mining address 
        """
        accountList = self.endPt.geth.personal.list_accounts()
        if(len(accountList) > 0):
            return accountList[0]
        else:
            return self.endPt.geth.personal.new_account(passphrase)
    
    def startMiner(self, numCores=1) -> bool:
        """
            `numCores` opt: number of Cores to mine
        """
        return  self.endPt.geth.miner.start(numCores)
    
    def stopMiner(self)-> bool:
        return self.endPt.geth.miner.stop()
    
    def getBalance(self):
        return self.endPt.eth.get_balance(self.getMinerAccountAddr())


    def getBlockNum(self):
        return self.endPt.eth.block_number
    