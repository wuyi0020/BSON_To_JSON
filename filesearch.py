import fnmatch
from os.path import join
from tkinter import filedialog
import os
# 指定搜尋之目錄
def Opendir():
    file_path = filedialog.askdirectory()
    if file_path  == None:
        return
    return file_path
# 回傳指定路徑的檔案樹
def FileTree(path):
    FileTree = os.walk(path,topdown=True)
    return FileTree
# 回傳檔案樹裡的所有檔案路徑
def FullFilePath(FileTree):
    dList = []  # 某檔案的 path
    sList = []  # 該檔案同一層的 目錄
    fList = []  # 該檔案的fullPathName 

    # 逐層向下
    for dirs, subdirs, files in FileTree:
        for f in files: 
            # 添加入 list
            # 目前檔案所在位置
            dList.append(dirs)
            # 目前檔案所在位置的同層級
            sList.append(subdirs)
            # dirs+f 組合成 檔案的fullpathname 
            fullpath = join(dirs,f)
            # 目前檔案的完整路徑 反斜線替換成斜線
            fList.append(fullpath.replace("\\","/"))
    return fList
# 傳入檔案路徑 及 文件副檔名 搜尋特定類型文件 預設為.txt檔
def FileSearch(FileTree,filetypes=[''] ):
    fL=[]
    for dirs, subdirs, files in os.walk(FileTree):
        for extension in ( tuple(filetypes) ):
            for filename in fnmatch.filter(files, extension):
                filepath = os.path.join(dirs, filename)
                if os.path.isfile(filepath):
                    fL.append(filepath)
    return fL





# FT = FileTree(Opendir())
# A = FullFilePath(FT)
# for f in range(len(A)):
#     print("{}".format(A[f]))
    