import os

def copyFIleSystem(path, toPath):
    "将一个路径 path 下的文件夹的结构复制到目标文件夹 toPath"
    mkdir(toPath)
    for subPath in os.listdir(path):   # 查看路径下的子文件夹
        absolutSubPath = os.path.join(path, subPath)  # 文件路径
        if os.path.isdir(absolutSubPath):  # 判断文件是否为文件夹
            if (subPath[0] != ".", subPath[0] != "$"):  # 判断是否是隐藏文件
                absoluteNewFolderPath = os.path.join(toPath, subPath)
                print(absoluteNewFolderPath)
                mkdir(absoluteNewFolderPath)
                copyFIleSystem(absolutSubPath, absoluteNewFolderPath)  # 递归查询
    if len(os.listdir(path)) == 0:
        addGitKeep(toPath)

def mkdir(path):
    "控制了报错的 os.mkdir"
    folder = os.path.exists(path)
    if (not folder):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print ("---  new folder...  ---")
        print ("---  OK  ---")
    else:
        print ("---  There is this folder!  ---")

def addGitKeep(path):
    "helper function 给 path 添加 .gitkeep, 进行版本控制"
    file = open(os.path.join(path, ".gitkeep"), "w")
    file.close()

def view(path, n=0):
    "查看 path 的文件夹结构，并在终端中用 markdown 格式打印结构树"
    for subPath in os.listdir(path):   # 查看路径下的子文件夹
        absolutSubPath = os.path.join(path, subPath)  # 文件路径
        if os.path.isdir(absolutSubPath):  # 判断文件是否为文件夹
            print("  " * n + "- " + subPath)
            view(absolutSubPath, n + 1)  # 递归查询
            
if __name__ == '__main__':
    path = "put your path here or use some func in os package to get path"
    toPath = "also, put your path here or use some func in os package to get path"
    
    copyFIleSystem(path, toPath)
    print('view 遍历结束！')
    view(toPath)
    print('view 遍历结束！')
