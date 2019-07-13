import matplotlib as pl
import numpy as np
import pandas as pd
#fname='c:/users/bin peng/onedrive - usst.edu.cn/桌面/publication/建筑结构学报（赵文昊）/previous data/draft.xls'
#data=pd.read_excel(fname)
File=open('C:/Users/Bin Peng/OneDrive - usst.edu.cn/桌面/Publication/PyWork/3/0－通道 0.dat')
#file=open('c:/users/2013-fwq/onedrive - usst.edu.cn/桌面/publication/pywork/3/0－通道 0.dat')
for i in range(0,1):
    File.readline()
Data= File.read()
print(Data)
