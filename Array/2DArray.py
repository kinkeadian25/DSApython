import numpy as np

twoDArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0 , [[10,11,12]], axis=1)
print(newTwoDArray)