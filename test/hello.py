import numpy as np
a=np.array([[1,2],[3,4],[5,6]])

print('array is',a)
##array is [[1 2]
## [3 4]
## [5 6]]


#print('未传递 Axis 参数。 在插入之前输入数组会被展开。' ,np.insert(a,3,[11,12]))
#在插入之前输入数组会被展开。 [ 1  2  3 11 12  4  5  6]


##print('沿轴 0 广播：' )
##print(np.insert(a,1,[11],axis = 0) )
##沿轴 0 广播：
##[[ 1  2]
## [11 11]
## [ 3  4]
## [ 5  6]]

##print('沿轴 1 广播：' )
##print(np.insert(a,1,11,axis = 1))
##array is [[1 2]
## [3 4]
## [5 6]]
##沿轴 1 广播：
##[[ 1 11  2]
## [ 3 11  4]
## [ 5 11  6]]
