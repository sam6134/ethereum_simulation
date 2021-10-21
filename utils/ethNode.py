from re import S
from web3 import Web3
import time

class ethNode:
    def __init__(self, addrPath: str, mode: str):
        """
            `addrPath`: path to ipc endpoint of eth-chain
        """
        self.minerLabel = ""
        self.publicIP = ""
        if(mode == 'IPC'):
            self.endPt =  Web3(Web3.IPCProvider(addrPath))
        elif(mode == 'HTTP'):
            self.endPt = Web3(Web3.HTTPProvider(addrPath))
            self.publicIP = ((addrPath.split("//")[-1]).split(":"))[0]

        else:
            raise Exception("Current mode {} not supported".format(mode))
    

    def getNodeIP(self) -> bool:
        if(self.publicIP == ""):
            raise Exception("Public IP not set")
        return self.publicIP

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
    

    def addPeer(self, node2, retries: int  = 10):
        """
            `enodeAddr`: address of enode to be Added
            `returns`: None / raises exception in case of an error
        """
        node2IP = node2.getNodeIP()
        enodeAddr = node2.getEnodeAddr().split('@')[0] + "@" + node2IP + ":30303?discport=0"
        try:
            retryCount = 0
            while(len(self.endPt.geth.admin.peers()) == 0 and retryCount < retries):
                retryCount += 1
                self.endPt.geth.admin.add_peer(enodeAddr)
            if(len(self.endPt.geth.admin.peers()) == 0):
                raise Exception("Cannot Add")
            print("Added peer {} Successfully".format(enodeAddr))
        except Exception as e:
            print(e)
            raise Exception("Error adding Node with address " + enodeAddr)
    

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
    

    def addLabelToMiner(self, labelName: str):
        """
            Sets a label for miner
        """
        self.minerLabel = labelName
        self.endPt.geth.miner.set_extra("minedbySmall")
        return


    def getMinerLabel(self) -> str:
        """
            returns the miner label if set
            else raises an exception
        """
        if(self.minerLabel == ""):
            raise Exception("Miner Label not Set")
        return self.minerLabel


    def startMiner(self, numCores=1) -> bool:
        """
            `numCores` opt: number of Cores to mine
        """
        self.getMinerAccountAddr()
        return  self.endPt.geth.miner.start(numCores)
    
    def stopMiner(self)-> bool:
        return self.endPt.geth.miner.stop()
    
    def getBalance(self):
        return self.endPt.eth.get_balance(self.getMinerAccountAddr())


    def getBlockNum(self):
        return self.endPt.eth.block_number
    