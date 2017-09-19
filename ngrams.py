import sys
import numpy as np
from pandas import *

def counttable(gajanan):
	arr = []
	array = [[] for i in range(len(myset)+1)]
	i = 1
	for word in myset:
		for word1 in myset:
			string = word + " " + word1
			array[i].append(data.count(string))
		i = i + 1

	j=1
	for word in myset:
		array[j][0:0] = [word]
		j=j+1

	j=0
	array[0].append("Table")
	for word in myset:
		array[0].append(word)
	
	#array[0].append(list)
	df = DataFrame(array)
	return df

def probtable(gajanan):
	arr = []
	array = [[] for i in range(len(myset)+1)]
	i = 1
	for word in myset:
		for word1 in myset:
			string = word + " " + word1
			array[i].append(data.count(string)/data.count(word))
		i = i + 1

	j=1
	for word in myset:
		array[j][0:0] = [word]
		j=j+1

	j=0
	array[0].append("Table")
	for word in myset:
		array[0].append(word)
	
	#array[0].append(list)
	df = DataFrame(array)
	return df

def counttableaddone(gajanan):
	arr = []
	array = [[] for i in range(len(myset)+1)]
	i = 1
	for word in myset:
		for word1 in myset:
			string = word + " " + word1
			array[i].append(data.count(string))
		i = i + 1

	j=1
	for word in myset:
		array[j][0:0] = [word]
		j=j+1

	j=0
	array[0].append("Table")
	for word in myset:
		array[0].append(word)
	
	#array[0].append(list)
	df = DataFrame(array)
	return df

def probtableaddone(gajanan):
	arr = []
	array = [[] for i in range(len(myset)+1)]
	i = 1
	for word in myset:
		for word1 in myset:
			string = word + " " + word1
			array[i].append((data.count(string)+1)/(data.count(word)+len(myset1)))
		i = i + 1

	j=1
	for word in myset:
		array[j][0:0] = [word]
		j=j+1

	j=0
	array[0].append("Table")
	for word in myset:
		array[0].append(word)
	
	#array[0].append(list)
	df = DataFrame(array)
	return df

def getIndex(df,myset,word1,word2):
	for i in range(len(myset)+1):
			if df.at[i,0] == word1:
				row = i
	for i in range(len(myset)+1):
			if df.at[0,i] == word2:
				column = i
	return row,column

def probsentence(string,df,myset):
	line = string.split()
	prob = 1
	for i in range(len(line)-1):
		r,c = getIndex(df,myset,line[i],line[i+1])
		prob = prob*df.at[r,c]
	return prob


filename = sys.argv[1]
if filename == "-h":
	print("Usage help : python ngrams.py <corpus_file_name> <sentence1> <sentence2>")
	print("For example: python ngrams.py Corpus.txt 'World is great' 'World has good people' ")

else:
	sentence1 =  sys.argv[2]
	sentence2 = sys.argv[3]
	with open(filename, 'r') as myfile:
    		data=myfile.read().replace('\n', '')
	data = data.replace(",", "")
	data = data.replace(".", "")
	a = data.split()
	myset1 = set(a)




	print(" ")
	print("*******************Sentence 1************************************")
	print(" ")
	print(sentence1)
	gajanan = sentence1
	b = gajanan.split()
	myset = set(b)
	dfc=counttable(gajanan)
	print(" ")
	print(" ")
	print("Bigrams count table:")
	print(dfc)
	dfp=probtable(gajanan)
	print(" ")
	print(" ")
	print("Bigrams probability table:")
	print(dfp)
	dfca=counttableaddone(gajanan)
	print(" ")
	print(" ")
	print("Bigrams count table with add-one smoothing")
	print(dfca)
	dfpa=probtableaddone(gajanan)
	print(" ")
	print(" ")
	print("Bigrams probability table with add-one smoothing:")
	print(dfpa)
	print(" ")
	print(" ")
	print("Probablity of the sentence is:")
	print(probsentence(gajanan,dfp,myset))
	print("Probablity of the sentence with add-one smoothing is")
	print(probsentence(gajanan,dfpa,myset))
	print(" ")
	print(" ")


	print("*******************Sentence 2************************************")
	print(" ")
	print(sentence2)
	gajanan = sentence2
	b = gajanan.split()
	myset = set(b)
	dfc=counttable(gajanan)
	print(" ")
	print(" ")
	print("Bigrams count table:")
	print(dfc)
	dfp=probtable(gajanan)
	print(" ")
	print(" ")
	print("Bigrams probability table:")
	print(dfp)
	dfca=counttableaddone(gajanan)
	print(" ")
	print(" ")
	print("Bigrams count table with add-one smoothing")
	print(dfca)
	dfpa=probtableaddone(gajanan)
	print(" ")
	print(" ")
	print("Bigrams probability table with add-one smoothing:")
	print(dfpa)
	print(" ")
	print(" ")
	print("Probablity of the sentence is:")
	print(probsentence(gajanan,dfp,myset))
	print("Probablity of the sentence with add-one smoothing is")
	print(probsentence(gajanan,dfpa,myset))	