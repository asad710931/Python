import sqlite3
import re

#Requler Expression

# '\d' all digit same as '[0-9]'
# '\D' no digit same as '[^0-9]'
# '\s' whitespace character
# '\S' non whitespace character
# '\w' All characters '[0-9a-zA-Z]'
# '\W' none characters '[^0-9a-zA-Z]'
# '+'  use + to groups them 
# '*'  fine all values place holder even value not exist
# '?'  make an char or sign optional
# '^'  inside act as a negative but outside fine first matches
# '$'  find last sign match or not like \.$ to fine . in end of string

phones='This is my number +8800-1919-710931 here are my family number +8801939403919 and my friend number 880-1887-989898'

#find all digit
pattern1='\d' 
#group digit with following digit  
pattern2='\d+'
#group digit with following digit
pattern3='\+?'+'\d{3}'+'-?'+'\d{4}'+'-?'+'\d{6}'
#group digit with without + with ? mark we can make preveiws sign optional
pattern4='\+?\d{3}-?\d{4}-?\d{6}'

#option #1
digit=re.findall(pattern4,phones)
#print(digit)

#option #2
phoneNumbers='+0(880)-1919-710931,'
#make parentheses optional
pattern5=r'\+?\d{1}-?\(\d{3}\)-?\d{4}-?\d{6}'

# -d=>[1-9]
pattern6=r'\+?[0-9]{1}-?\([0-9]{3}\)-?[0-9]{4}-?[0-9]{6}'

#if you need certain numbers then use [from-to] instead of \d
pattern7=r'\+?[0-5]{1}'

#match with this certain numbers if number doesnt match with given value return empty list
pattern8=r'\+?[0-9]{1}\([0-9]{3}\)-?[19]{4}-?[13579]{6}'

myNumber='880-1821-710931' #+880-1601-710931,+880-1919-710931'

#Using OR Oparation 
pattern9=r'\+?[0-9]{3}-?(?:1919|1601)-?\d{6}'

regex=re.compile(pattern5)
data=re.findall(regex,myNumber)
#print(data)

#group and groups using RE
pattern_group=r'(\d{3})-?(\d{4})-?(\d{6})'

#matched=re.compile(pattern_group).match(myNumber)
matched=re.compile(pattern_group).match(myNumber)
'''
if matched: 
    print('group:',matched.group())
    print('groups:',matched.groups())
    print(matched[2])
    print('Country Code : ',matched.group(1))
'''
#named Group  pettern RE
myNumbers='880-1821-710931 +880-1601-710931 +880-1919-710931'
named_pattern=r'\+?(?P<Country_code>\d{3})-?(?P<Area_code>\d{4})-?(?P<Line_Number>\d{6})'


named_group=re.compile(named_pattern).finditer(myNumbers)
datas=[]
for m in re.compile(named_pattern).finditer(myNumbers):
    #print(m.group(0))
    #print(m.groupdict())
    data={**m.groupdict()}
    data['full_number']=m.group(0)
    datas.append(data)

#print(datas)

#Letter using in RE
text='Hi writing code should be fun and cool 24/7.' 

#Every single word from strings
tpettern='[a-z]' #or \w
#grouping word with spaces Capital none Capital letters and numbers
tpettern1='\w+' #or [a-z]+
#grouping word with spaces Capital none Capital letters
tpettern2='[a-zA-Z]+'
#grouping word with spaces Capital none Capital letters and numbers with period and splashes
tpettern3='[0-9a-zA-Z.\/\?]+'

letters=re.findall(tpettern3,text)
#print(' '.join(letters))

#metacharacters line of

#  ^ = caret sign 
# ^ - the start of string with given value 
#fine first value match with ^[A-Z] 
print(re.findall('^[A-Z]','A lion is hunting')) 
print(re.findall('^[A-Z]','he is hunting in Jungle')) 

#[^0-9] matches everything but [0-9] because ^ 

#print(re.findall('[^0-9A-Z]+','This Phone ring 33 time in 4 day'))
signList=re.findall('[^a-zA-Z0-9 ]','This Phone [loud] ring (33) time i % n 4 day cost me $90')
print(signList)

#$ sign indicate that if \.$ string is end with specifice char (period) or not 
strings_text='Hi, have you ever been in a mosque to understand the value of faith?'
print(re.findall('\?$',strings_text))
print(len(re.findall('\s',strings_text)))

have_it=True if re.findall('\?$',strings_text)==['?'] else False


print(have_it)

#=============END OF REGULAR EXPRESSION FOR BEGINEER====================



