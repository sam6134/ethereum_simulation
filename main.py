from utils.ethNode import ethNode
from utils.simulation import simulation

node1 = ethNode("network_data/eth_data1/geth.ipc")
node2 = ethNode("network_data/eth_data2/geth.ipc")

node1.addPeer(node2.getEnodeAddr())

# uncomment below for simulation

# mySimulation = simulation(node1, node2, 10)
# mySimulation.start()

print(node1.getBlockNum(), node2.getBlockNum())