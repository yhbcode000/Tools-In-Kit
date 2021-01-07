import os
import numpy as np

""" 读取图片 """
def getFileContent(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 存入本地 """
def saveFileContent(bfile, filePath):
    with open(filePath, 'wb') as bw:
        bw.write(bfile)
        return 1

""" 获取文件名 """
def getFileName(value, digits):
    result = str(value)
    digits -= len(result)
    for i in range(digits):
        result = "0" + result
    return result + ".png"

""" 替换图片 """
def replaceMent(start, digits):
    fileName = getFileName(start[0], digits)
    filePath = os.path.join(os.getcwd(), "interpolated_frames", fileName)
    startFrame = getFileContent(filePath)
    for j in range(start[0], start[0]+4):
        fileName = getFileName(j, digits)
        filePath = os.path.join(os.getcwd(), "interpolated_frames", fileName)
        saveFileContent(startFrame, filePath)
    return True

digits = len("000000000000002")
startsAndEnds = np.array([[2873, 3001, 3245, 3841, 3997, 4421, 4573, 4701, 4817, 4853, 5421, 5705, 5869, 5909, 5945, 6237, 6549, 7093, 7165, 7217, 7289, 7365, 7497, 7917, 8049, 8249, 8285, 8357]])

np.apply_along_axis(lambda x : replaceMent(x, digits), 0, startsAndEnds)

# continuousList = [i for i in range(337,441,4)]
