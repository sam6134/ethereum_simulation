from utils.ethNode import ethNode
import time

class simulation:
    def __init__(self,node1: ethNode, node2: ethNode, numTimes: int, blockErr: int = 2):
        self.node1 = node1
        self.node2 = node2
        self.numTimes = numTimes
        self.blockErr = blockErr
    
    def connectNodes(self):
        if(self.node1.isConnected and self.node2.isConnected):
            self.node1.addPeer(self.node2)
        else:
            raise Exception("Nodes are not reachable")

    def start(self):
        self.connectNodes()

        self.node1.addLabelToMiner("minedbySmall")
        self.node2.addLabelToMiner("minedbyBig")

        numBlocksSmall = 0
        numBlocksBig = 0
        currBlocks = 0
        prevBlocks = 0

        for _ in range(100):
            self.node1.startMiner()
            self.node2.startMiner()
            time.sleep(10)
            self.node1.stopMiner()
            self.node2.stopMiner()
        
            while(abs(self.node1.getBlockNum() - self.node2.getBlockNum()) > self.blockErr):
                time.sleep(1)
        
            print("Num Blocks-", self.node1.getBlockNum())
            currBlocks = self.node1.getBlockNum()
            for blockNum in range(prevBlocks,currBlocks):
                blockTag = self.node1.endPt.toText(self.node1.endPt.eth.get_block(blockNum)["extraData"])
                if(blockTag == "minedbySmall"):
                    numBlocksSmall += 1
                elif(blockTag == "minedbyBig"):
                    numBlocksBig += 1

            try:
                print(self.node1.getBalance()/self.node2.getBalance())
                print(numBlocksSmall/ numBlocksBig)
            except:
                pass

            prevBlocks = currBlocks


        
