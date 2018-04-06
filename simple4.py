# 6 Apr 10 AM
#  https://www.youtube.com/watch?v=FmpDIaiMIeA&index=3&list=PLVZqlMpoM6kbaeySxhdtgQPFEC5nV7Faa
#    Bradon Rohrer

# https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html


import numpy as np

np.set_printoptions(precision=2)


#a = np.dtype(float)
tt = np.arange(49).reshape(7,7)
a = np.array(tt, dtype=np.float64)

a = a * -1.0

a[3,3] = 1.0
a[3,5] = 1.0
a[4,4] = 1.0
a[3,3] = 1.0
a[5,5] = 1.0


t2 = np.arange(49).reshape(7,7)
TheTarget = np.array(t2, dtype=np.float64)
TheTarget = np.arange(9).reshape(3,3)

TheTarget[0,0] = 1
TheTarget[1,0] = -1.0
TheTarget[2,0] = -1.0

TheTarget[0,1] = -1.0
TheTarget[1,1] = 1
TheTarget[2,1] = -1.0

TheTarget[0,2] = -1.0
TheTarget[1,2] = -1.0
TheTarget[2,2] = 1

# ----------------------------------
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
# ----------------------------------

def CompareBlockToTarget( theBlock, Target, atUL ):

    isInside = False
    TargetSize = Target.shape
    theBlockSize = theBlock.shape
    for i in range(0,theBlockSize[1]):
        for k in range(0,theBlockSize[0]):
          if (i+1 <= TargetSize[1]) and (k+1 <= TargetSize[0]):
            if Target[i + atUL[0], k + atUL[1]] == theBlock[i, k]:
              theBlock[i, k] = Target[i + atUL[0], k + atUL[1]] * theBlock[i, k]
            else:
              theBlock[i, k] = 1.0 / Target.size

    return theBlock

b = CompareBlockToTarget( a, TheTarget, [0, 0])

print("b is ")
#print("%7.2f", b)

print(b)