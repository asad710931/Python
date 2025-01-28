
texts='Some of text just have to been in \nnew line rest of them \nmore  new line'
# #1 Genaral and basic method to working with files

myfile=open('mytext1.txt',mode='w',encoding='utf-8')
myfile.write(texts)
print('files has been created')
myfile.close()
print('files closed')

myfileR=open('mytext1.txt',encoding='utf-8') 
mytext = myfileR.read()
print(mytext)
myfileR.close()

# #2 Genaral and basic method to working with files
with open('mytext.txt',mode='w',encoding='utf-8') as txtFile:
    txtFile.write('Some of text just have to been in \nnew line rest of them \nmore  new line')
    print('written on files')

with open('mytext.txt',encoding='utf-8') as txtFile:
    print(txtFile.read())
print(txtFile.closed)

inp1=input('Enter Name of Files : ')
inp2=input('Write some text on files : ')

with open(f'{inp1}.csv',mode='w',encoding='utf-8') as file:
    file.write(inp2)
    print('File has been created')

print(open(f'{inp1}.csv',encoding='utf-8').read())

occupations=['Programmer','Student','CFO','Unemployee','Broker','Oparetor','Docs Writer']

file=open('data.csv',mode='w',encoding='utf-8')
for i in range(len(occupations)):
    file.write(f'{i},{occupations[i]},{occupations[i]}\n')
print('file created')


data=['Asad','Programmer','Sabed','Student','Riyad','Student','Kamal','CFO','Hossain','Broker','Tipo','Oparetor','Dolan','Docs Writer','Belal','CFO']
file=open('newData.csv',mode='w',encoding='utf-8')

na=data[0:-1:2]
oc=data[1:-1:2]
for i in range(len(na)+1):
    try:
        file.write(f'{i},{na[i]},{oc[i]}\n')
    except :
        print('Problems')

print('files has been created')
file.close()

for i in range(len(data)):
    try:
       if not i%2:
        print(data[i],data[i+1])
        #file.write(f',{data[i]},{data[i+1]}\n')
        
        
    except:
        print('out of range')
  