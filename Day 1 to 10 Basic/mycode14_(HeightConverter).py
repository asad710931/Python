import sys
import os
import math
import re

print('======CONVERT CM TO FEET OR VICE VERSA')
getInput=input('Type your options:')

def PrintReturn():
    print('If want to convert feet to cm then use\n=> ft/feet/f\nIf want to convert cm to feet use \n=>cm/centimeter/c \n\n')

def getYouHeightConverted():
    if re.search('f|feet|fe|f|fet|ft',getInput.lower()):
        print(f'Your Choose feet to cm')
        feet=int(input('Type feet:'))
        inch=int(input('Type Inch:'))
        totalInch=inch+(feet*12)
        yourCM=totalInch/0.3937
        print(f'You are {round(yourCM)} centimeter tall')
    elif re.search('c|centi|cm|centimeter|cen|cantimitar|centimitar|cen|meter|cenmeter',getInput.lower()):
        print(f'Your Choose cm to feet')
        totalCM=int(input('Type cm:'))
        getTotalInch=totalCM*0.3937
        getFeet=math.floor(getTotalInch/12)
        getRestInch=round(getTotalInch%12)
        print(f'You are {getFeet}\' and {getRestInch}" tall')

    else:
        PrintReturn()
getYouHeightConverted()

        