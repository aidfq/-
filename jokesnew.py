import csv
import math
import itertools
from collections import Counter
import xlrd
import numpy
import xlsxwriter
import xlwt

#Item-based collaborative filtering with Adjusted cosine similarity

num_jokes=100
num_users=23500
#24983

userLines=None
reader=[]
userLines=numpy.loadtxt(open('/home/handing/Jokes-Recommendation-System-master/jester-data-2.csv','rb'),delimiter=',',skiprows=0)
print(userLines)
# with open('/home/handing/Jokes-Recommendation-System-master/jester-data-2.csv', 'r') as f:
#     for i in range(24983):
#         reader.append(f.readline())
#     print(reader)
#     userLines=list(reader)
#print(userLines)
jokesscore=numpy.empty([100,23500])
userscore={}
usermean=[0]*num_users
x = []

userLines.astype(numpy.float)
print(userLines)


for i in range(0,num_users):
#     for userValue in userLines[i]:
#         userscore[i]=list(map(float,userValue))
#     sums=0
#     notnull=0
#     print(userscore)
    sums=0
    notnull=0
    for j in range(1,num_jokes):
        #print (i,j)
        if userLines[i][j]!=99:
            sums+=userLines[i][j]
            
#             notnull+=1
    usermean[i]=sums/userLines[i][0]

vectorMagnitudes = [0]*100
temp=[0]*100
for j in range(1,num_jokes):
#     jokesscore[j]=[]
    for i in range(0,num_users-1):
        if userLines[i][j]==99:
            jokesscore[j][i]=0
        else:
            jokesscore[j][i]=(userLines[i][j]-usermean[i])
        temp[j]+=jokesscore[j][i]**2
#     for x in jokesscore[j][*]
    
#     temp=[x **2 for x in jokesscore[j]]
    vectorMagnitudes[j]=(math.sqrt(temp[j]))
#     if vectorMagnitudes[j]==0:
#         print('helloworld')
print(jokesscore)
# # with open('./joke_similarities.xls', 'wb') as f:
# workbook=xlwt.Workbook(encoding = 'ascii')
# worksheet = workbook.add_sheet('My Worksheet')
# #     writer=xlwt.writer(f)
# #     writer.writerow(['jokeA', 'jokeB', 'similarity'])

# # jokes=list(jokesscore)
# # print(jokes)
# for i in range(0,99):
#     for j in range(i+1,100):
#         vectorA=jokesscore[i]
#         vectorB=jokesscore[j]
#         similarity=sum([a * b for a, b in zip(vectorA, vectorB)])
#         similarity/=(vectorMagnitudes[i] * vectorMagnitudes[j])
            
#         worksheet.write(i, j,  '%.4f'%similarity)
# workbook.save('Excel_Workbook.xls')
            
# #             writer.writerow([jokeA, jokeB, '%.4f'%similarity])
            

    
    

with open('./joke_similarities.csv', 'w',encoding='utf8') as f:
    writer=csv.writer(f)
    #writer.writerow(['jokeA', 'jokeB', 'similarity'])
#     jokes=list(jokesscore)
    for i in range(0,99):
        for j in range(i+1,100):
            vectorA=jokesscore[i]
            vectorB=jokesscore[j]
            similarity=sum([a * b  if a!=99 and b!=99 else 0 for a, b in zip(vectorA, vectorB)])
            if vectorMagnitudes[i]<(0.00000001):
                similarity=0
            else:
                if vectorMagnitudes[j]<(0.0000001):
                    similarity=0
                else:
                    similarity/=(vectorMagnitudes[i] * vectorMagnitudes[j])
                    writer.writerow([i, j, '%.4f'%similarity])
print('end')
            