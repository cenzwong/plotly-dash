# activate R magic
%load_ext rpy2.ipython

%%R
HSI<-read.csv("./data/Hang Seng Historical Data.csv",header=T)

