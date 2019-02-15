# Introduction

`batquant` is a package that helps developers, researchers to quickly get Vietnam financial data. Since Vietnam is not well-supported by famous platform like Bloomberg, Reuters, Yahoo, Google, we were inspired to develop our own data package that serves Vietnam data.

# Recent changes

## v0.1.0 - 20190215:

- First version
- Data available: trading data only

## Incoming: v0.2.0:

##### Add more data:

- reference prices (ceiling, floor, ref price...)
- stock info (company name, shareout, list of stocks)

##### Exception handler

##### Reference object to lookup for fields

# Installation

`pip install batdata`

# Usage

## Init data object

```
import batdata
vnd = batdata.Vnd() # Data from VND api
```

## Getting data

```
# historical data of HPG from 2018-01-01 to 2018-12-31
data = vnd.hist("HPG","close","20180101","20181231")

jsonData = data.json # getting data as json
dfData = data.df # getting data as pandas DataFrame

# fromTime and toTime can also be python datetime objects
fromTime = datetime.datetime(2018,01,01)
toTime = datetime.datetime(2018,12,31)
hpgHist = vnd.hist("HPG","close",fromTime,toTime)

# historical OHLC data of HPG, MSN
hpgHistWeekly = vnd.hist(["HPG","MSN"],["open","high","low","close"],"20180101","20181231",interval="w")

# last price
hpgLast = vnd.curr("HPG","last")


```

# TODO

## Financial fields reference

## More data
