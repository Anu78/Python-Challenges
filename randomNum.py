import time
def genRandom(low, high):
    epochNS = time.time_ns()
    epochS = time.time()
    print(epochS / epochNS)



amount = int(input("Amount: "))
for boo in range(amount):
    genRandom(1,100)