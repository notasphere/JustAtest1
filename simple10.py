# 7 Apr 6:14 PM
#  https://www.youtube.com/watch?v=FmpDIaiMIeA&index=3&list=PLVZqlMpoM6kbaeySxhdtgQPFEC5nV7Faa
#    Bradon Rohrer

# https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html


import numpy as np

#np.set_printoptions(precision=3)
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

a = np.arange(81).reshape(9, 9)
a = np.asfarray(a,float)
a[:] = -1.0

a[1,1] = a[1,7] = 1.0
a[2,2] = a[2,6] = 1.0
a[3,3] = a[3,5] = 1.0
a[4,4] = a[4,4] = 1.0
a[5,5] = a[5,3] = 1.0
a[6,6] = a[6,2] = 1.0
a[7,7] = a[7,1] = 1.0

theFilter = np.arange(9).reshape(3, 3)
theFilter = np.asfarray(theFilter,float)
theFilter[:] = -1.0


theFilter[0,0] = 1
theFilter[1,1] = 1
theFilter[2,2] = 1

# ----------------------------------
"""
print(a)
ss = ""
kk = 0
for i in range(0,7):
    ss = ""
    for k in range(0,7):
        if a[i, k] == 5:
          ss = ss + "M"
        else:
          ss = ss  + str(a[i, k])
        kk += 1    

    ss = str(kk) + " " + ss
    print(' {:>15}'.format(ss))
"""
# ----------------------TargetSize[1]------------

def CompareBlockToFilter( theBlock, atUL ):

    filterWindow = np.arange(9).reshape(3, 3)
    filterWindow = np.asfarray(filterWindow, float)
    filterWindow[:] = -1.0

    filterWindow[0, 0] = 1
    filterWindow[1, 1] = 1
    filterWindow[2, 2] = 1

    filterWindowMatch = filterWindow
    # --------------------

    iBlock = atUL[0]  # down
    kBlock = atUL[1]  # across

    filterWindowMatchSum = filterWindowMatchCalc = 0
    t = ""

    for i in range(0, filterWindow.shape[0]):

        for k in range(0, filterWindow.shape[1]):
          blockElement = theBlock[iBlock, kBlock]
          filterWindowElement = filterWindow[i, k]

          filterWindowMatchProd = filterWindowElement * blockElement
          filterWindowMatchSum += filterWindowMatchProd


          t = " " +  t + "  " + str(filterWindowMatch[i, k])

          kBlock += 1

        iBlock += 1       # move down
        kBlock = atUL[1]  # reset across
    # --------------------------------------------------

    filterWindowMatchCalc = filterWindowMatchSum / filterWindow.size
    filterWindowMatch[i, k] = filterWindowMatchCalc

    return filterWindowMatchCalc, filterWindowMatch
# ------------------------------------

def poolingDOLD(theBlock, atUL, stridePool):

    tmpSize = stridePool
    tmpMatrix = np.arange(stridePool * stridePool).reshape(stridePool, stridePool)
    tmpMatrix = np.asfarray(tmpMatrix, float)
    tmpMatrix[:] = 0

    [ii, kk] = atUL
    #ii = atUL[0]
    #kk = atUL[1]

    if ii > theBlock.shape[0] - 1:
        ii = theBlock.shape[0] - 1

    if kk > theBlock.shape[1] - 1:
        kk = theBlock.shape[1] - 1

    for i in range(0, tmpMatrix.shape[0]):
        for k in range(0, tmpMatrix.shape[1]):
          if ii < theBlock.shape[0]:
            tmpMatrix[i, k] = theBlock[ii, kk]
            ii += 1

        kk += 1
        ii = 0

        if kk >= theBlock.shape[0] - 1:
          break


    maxPoolDD = np.max(tmpMatrix)
    #maxPoolDD = np.asfarray(maxPoolDD, float)
    return maxPoolDD
    
    
# ------------------------------------
def poolingD(theBlock, atUL, stridePool):

    #
    # Max within theBlock
    # from atUL
    # to atUL + (stridePool, stridePool)
    #

    curBlockX = atUL[0]
    curBlockY = atUL[1]

    blockMax = 0.0
    isDone = False

    # do ... until isDone
    while not isDone:
        if (blockMax < theBlock[curBlockX, curBlockY]):
            blockMax = theBlock[curBlockX, curBlockY]

        curBlockX += 1
        curBlockY += 1

        isDoneX = (curBlockX == (atUL[0] + strideSize)) or \
                  (curBlockX >= theBlock.shape[0])

        isDoneY = (curBlockY == (atUL[1] + strideSize)) or \
                  (curBlockY >= theBlock.shape[1])

        isDone = (isDoneX and isDoneY)

        if isDone:
            return blockMax

        if isDoneX:
            # reset X
            curBlockX = atUL[0]

        if isDoneY:
            # reset Y
            curBlockY = atUL[1]

# ------------------------------------

qq = np.arange(49).reshape(7, 7)
qq = np.asfarray(qq, float)
qq[:] = -1.0

for ii in range(0, a.shape[0] - 2):
 for kk in range(0, a.shape[1] - 2):

   (filterSum, filtWin) = CompareBlockToFilter(a, [ii, kk])

   # ReLU
   #if filterSum < 0:       filterSum = 0

   qq[ii, kk] = filterSum

print("\nqq is")
print(qq)


strideSize = 2

if (a.size % 2) != 0:
  poolQshape = (qq.shape[0] + 1) / strideSize
else:
  poolQshape = (qq.shape[0] + 0) / strideSize

poolQshape = np.asarray(poolQshape, int)
poolQ = np.arange(poolQshape * poolQshape).reshape(poolQshape, poolQshape)
poolQ = np.asfarray(poolQ, float)
poolQ[:] = -5.8

#poolUL = [0, 0]
ii = kk = 0

for i in range(0, poolQ.shape[0]):

 for k in range(0, poolQ.shape[1]):
    if k == 0:
        kk = 0  # reset kk when k auto resets
    poolMaxR = poolingD(qq, [ii, kk],  strideSize)
    poolQ[i, k] = poolMaxR
    kk += strideSize

 ii += strideSize

print("\nstrideSize = ", strideSize, " = \n\n", poolQ)
   # ReLU
   #if b[ii,kk] < 0:
   #    b[ii, kk] = 0

   #b[ii, kk] = FiltSum
   #a = b


