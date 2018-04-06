# 6 Apr 10:09 PM
#  https://www.youtube.com/watch?v=FmpDIaiMIeA&index=3&list=PLVZqlMpoM6kbaeySxhdtgQPFEC5nV7Faa
#    Bradon Rohrer

# https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html


import numpy as np

np.set_printoptions(precision=2)


a = np.arange(81).reshape(9,9)
a.astype(float)

#a = a * 0.0
a[:] = -1.0

a[1,1] = a[1,7] = 1.0
a[2,2] = a[2,6] = 1.0
a[3,3] = a[3,5] = 1.0
a[4,4] = a[4,4] = 1.0
a[5,5] = a[5,3] = 1.0
a[6,6] = a[6,2] = 1.0
a[7,7] = a[7,1] = 1.0

theFilter = np.arange(9).reshape(3,3)
theFilter.astype(float)
theFilter[:] = -1.0


theFilter[0,0] = 1
theFilter[1,1] = 1
theFilter[2,2] = 1

# ----------------------------------
print      (a)
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
# ----------------------TargetSize[1]------------

def CompareBlockToFilter( theBlock, Target, atUL ):

    iBlock = atUL[0]
    kBlock = atUL[1]

    TargetSize = Target.shape
    TargetSum = 0
    t = ""

    for i in range(0, TargetSize[1]):

        for k in range(0, TargetSize[0]):
          BlockElement = theBlock[iBlock, kBlock]
          TargetElement = Target[i, k] * BlockElement
          kBlock += 1
          TargetSum += TargetElement
          t = t + "   " + str(TargetElement)

        iBlock += 1
        kBlock = atUL[1]



    TargetQ = TargetSum / Target.size
    fSum = TargetQ
    return (theBlock, fSum )

(b, FiltSum) = CompareBlockToFilter( a, theFilter, [3, 3] )

print("\nFiltSum is %.5f" % FiltSum, "\n\nb is ")
#print("%7.2f", b)

print(b)
