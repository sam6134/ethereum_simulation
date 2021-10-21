import matplotlib.pyplot as plt
file1 = open('simul.txt', 'r')
Lines = file1.readlines()

ratioBalance = []
ratioBlock  = []
numBlocks = []

for lineNo in range(0,len(Lines),3):
    numBlockLine = (Lines[lineNo].split("-"))[-1]
    ratioBalanceLine = Lines[lineNo+1]
    ratioBlockLine = Lines[lineNo+2]

    numBlocks.append(int(numBlockLine))
    ratioBalance.append(float(ratioBalanceLine))
    ratioBlock.append(float(ratioBlockLine))

# print(numBlocks, ratioBalance, ratioBlock)
n = len(numBlocks)
plt.plot(numBlocks,ratioBalance)
plt.scatter(numBlocks[::10],ratioBalance[::10])
plt.plot(numBlocks,ratioBlock)
plt.scatter(numBlocks[::10],ratioBlock[::10])
plt.plot(numBlocks,[0.5]*n)
plt.scatter(numBlocks[::10],([0.5]*n)[::10])

plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend(['Balance_R', 'Block_R', 'Ideal'])
plt.show()







