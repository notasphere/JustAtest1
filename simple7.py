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

qq = np.arange(49).reshape(7, 7)
qq = np.asfarray(qq, float)
qq[:] = -1.0


for ii in range(0, a.shape[0] - 2):
 for kk in range(0, a.shape[1] - 2):

   (filterSum, filtWin) = CompareBlockToFilter(a, [ii, kk])
   qq[ii, kk] = filterSum

print(qq)

   # ReLU
   #if b[ii,kk] < 0:
   #    b[ii, kk] = 0

   #b[ii, kk] = FiltSum
   #a = b


