import os
 
 
# Specify path
path = 'C:/Users/Karol/Desktop/excel-python/note/PJ.txt'
 
# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)