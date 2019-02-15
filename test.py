import batdata

vnd = batdata.Vnd()

data = vnd.curr("HPG", "close")
print(data.df)
data = vnd.curr(["HPG","MSN","VNM"],["open","high","low","close"])
print(data)
data = vnd.hist(["HPG","MSN","VNM"],"open")
print(data.df)
data = vnd.hist(["HPG","MSN","VNM"],"open","20180101")
print(data)
data = vnd.hist(["HPG","MSN","VNM"],"open","20180101","20181231")
print(data)
data = vnd.hist("HPG,MSN",["open","close"],"20180101","20181231")
print(data)
