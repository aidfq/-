import csv
import math
import itertools
from collections import Counter

#Item-based collaborative filtering with Adjusted cosine similarity

num_jokes=100

userscore=[99]*101
jid=0
jscore=0

print ("\n*****************************************************************")

print ("\n\n\n\n\n             Welcome to use Joke Recommendation App")

print ("\n\n\n\n\n*****************************************************************\n\n")

while True:
    jid, jscore = input("Enter the joke id and your rating here (Enter q q to stop): ").split()
    if jid=='q':
        break
    else:
        userscore[int(jid)]=int(jscore)

js=[]
with open('./joke_similarities.csv', 'r') as f:
    reader=csv.reader(f)
    joke_simi=[tuple(float(n) for n in line.split(",")) for line in f]
    length=len(joke_simi)

userLines=None
with open('./jester-data-2.csv', 'r') as f:
    reader=csv.reader(f)
    userLines=list(reader)

predition={}
for j in range(1,1+num_jokes):
    if userscore[j]==99:
        simi_sum=0
        weighted_sum=0
        predit=0
        for k in range(0,length):
            if joke_simi[k][0]==j:
                if userscore[int(joke_simi[k][1])]!=99:
                    simi_sum+=abs(joke_simi[k][2])
                    weighted_sum+=joke_simi[k][2]*userscore[int(joke_simi[k][1])]
            elif joke_simi[k][1]==j:
                if userscore[int(joke_simi[k][0])]!=99:
                    simi_sum+=abs(joke_simi[k][2])
                    weighted_sum+=joke_simi[k][2]*userscore[int(joke_simi[k][0])]
        if simi_sum<(0.00000001):
            predit='none'
        else:
            predit=weighted_sum/simi_sum
            predition[j]=float('%.4f'%predit)
predition=sorted(predition.items(), key = lambda x : x[1], reverse=True) 

print ("\nYour jokes recommendation are")
print (predition[1:6])
print ("\n")




