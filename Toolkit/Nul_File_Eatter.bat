::@author Discover304 hobart.yang@qq.com

:: 目的是删除nul文件
:: the purpose of this file is delet nul file

:: 把无法删掉的nul文件拖到这个上就ok了
:: drag nul file into this .bat file. 

DEL /F /A /Q \\?\%1
RD /S /Q \\?\%1   