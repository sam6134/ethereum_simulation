from utils.ethNode import ethNode
import time

class simulation:
    def __init__(self,node1: ethNode, node2: ethNode, numTimes: int):
        self.node1 = node1
        self.node2 = node2
        self.numTimes = numTimes
    
    def start(self):
        self.node1.startMiner(3)
        self.node2.startMiner(1)

        for _ in range(self.numTimes):
            time.sleep(10)
            print("Number of Blocks", self.node1.getBlockNum(), self.node2.getBlockNum())
            print(self.node1.getBalance()/self.node2.getBalance())

        self.node1.stopMiner()
        self.node2.stopMiner()
