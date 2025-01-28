import sys
import os
import math

highNum,lowNum,hightList=193,165,[]

for i in range(50):
    if lowNum!=highNum:
        lowNum = lowNum+2
        hightList.append(lowNum)

totalInAll=0
for h in hightList:
    totalOfOne=h*10
    totalInAll+=totalOfOne

getTheAvgCM=totalInAll/(len(hightList)*10)
getTotalInch=getTheAvgCM*0.3937
getFeet=math.floor(getTotalInch/12)
getRestInch=round(getTotalInch%12)

print(f'Average man Height \n====================\nIn centimeters:{getTheAvgCM}\nIn Feets:{getFeet}\'-{getRestInch}"')
        