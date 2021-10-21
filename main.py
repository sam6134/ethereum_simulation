from logging import exception
from utils.ethNode import ethNode
from utils.simulation import simulation
from web3 import Web3
import time

# node1 = Web3((Web3.HTTPProvider('http://52.179.16.71:8545')))
# node2 = Web3((Web3.HTTPProvider('http://20.83.152.84:8545')))

# print(node1.isConnected(), node2.isConnected())
# print(node1.geth.admin.nodeInfo()["enode"], node2.geth.admin.nodeInfo()["enode"])

# enodeAddr = node2.geth.admin.nodeInfo()["enode"].split('@')[0]
# # exit(1)

# while(len(node1.geth.admin.peers()) == 0):
#     print(node1.geth.admin.add_peer(enodeAddr+"@20.83.152.84:30303?discport=0"))
#     print(node1.geth.admin.peers())

# accountList = node1.geth.personal.list_accounts()
# if(len(accountList) > 0):
#     minerAcct1 = accountList[0]
# else:
#     minerAcct1 = node1.geth.personal.new_account("1234")

# accountList = node2.geth.personal.list_accounts()
# if(len(accountList) > 0):
#     minerAcct2 = accountList[0]
# else:
#     minerAcct2 = node2.geth.personal.new_account("1234")

# node1.geth.miner.set_extra("minedbySmall")
# node2.geth.miner.set_extra("minedbyBig")
# numBlocksSmall = 0
# numBlocksBig = 0
# currBlocks = 0
# prevBlocks = 0
# for _ in range(100):
#     node1.geth.miner.start()
#     node2.geth.miner.start()
#     time.sleep(10)
#     node1.geth.miner.stop()
#     node2.geth.miner.stop()
#     while(abs(node1.eth.get_block_number() - node2.eth.get_block_number()) > 2):
#         time.sleep(1)
    
#     print("Num Blocks-",node1.eth.get_block_number())
#     currBlocks = node1.eth.get_block_number()
#     for blockNum in range(prevBlocks,currBlocks):
#         blockTag = node1.toText(node1.eth.get_block(blockNum)["extraData"])
#         if(blockTag == "minedbySmall"):
#             numBlocksSmall += 1
#         elif(blockTag == "minedbyBig"):
#             numBlocksBig += 1

#     try:
#         print(node1.eth.get_balance(minerAcct1)/node2.eth.get_balance(minerAcct2))
#         print(numBlocksSmall/ numBlocksBig)
#     except:
#         pass

#     prevBlocks = currBlocks


node1 = ethNode("http://52.179.16.71:8545", "HTTP")
node2 = ethNode('http://20.83.152.84:8545', "HTTP")

mySimulation = simulation(node1, node2, 100)

mySimulation.start()


