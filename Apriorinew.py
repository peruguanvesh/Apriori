import itertools
import pdb

def support_count(support,transactions_count):
	support_count=(support/100)*transactions_count
	if support_count is int:
		return(support_count)
	else:
		return(int(support_count)+1)

f=open('transactions.txt','r')

def Unique_one():
	unique_one=[]
	for line in f.readlines():
		stri=line.strip('\n')
		spli=stri.split(',')
		for a in spli:
			if a not in unique_one:
				unique_one.append(a)
	print('Unique items are:', unique_one)
	return(unique_one)

def Unique_one_count(unique_one):
	unique_one_count={}
	for item in unique_one:
		f.seek(0)
		count=0
		for line in f.readlines():
			stri=line.strip('\n')
			spli=stri.split(',')
			if (item in spli)==True:
				count=count+1
		unique_one_count[item]=count
	print('count of unique items:', unique_one_count)
	return(unique_one_count)

def frequent1_items(unique_one_count):
	f1=[]
	for item in unique_one_count:
		if unique_one_count[item]>=support_count(i,j):
			f1.append(item)
	print('frequent1_items are:', f1)
	return(f1)

def twoset_combination(frequent_item):
	twoset_combination=[]
	for twoset in itertools.combinations(frequent_item,2):
		twoset_combination.append(twoset)
	return(twoset_combination)

def combination(fi,nfi,l):
	combinations=[]
	combination_tupl=[]
	if l<=1:
		print('end of algorithm')
	else:
		for item in itertools.combinations(fi,2):
			if len(set(item[0])&set(item[1]))==(len(set(item[0]))-1):
				item_frequent=set(item[0]).union(set(item[1]))
				count=0
				for item in nfi:
					if (set(item)<set(item_frequent))==False:
						count=count+1
				if count==len(nfi):
					if item_frequent not in combinations:
						combinations.append(item_frequent)
		for item in combinations:
			combination_tupl.append(tuple(item))
		print('the candidate combinations are:', combination_tupl)
		count_candidate_items(combination_tupl)
	return(combination_tupl)

def count_candidate_items(combinations):
	items={}
	for element in combinations:
		count=0
		f.seek(0)
		for line in f.readlines():
			stri=line.strip('\n')
			spli=stri.split(',')
			if len(set(element))==len(set(element)&set(spli)):
				count=count+1
		items[element]=count
	print('count of candidate items:', items)
	frequent_items(items)
	return(items)
nfi=[]
def frequent_items(items):
	fi=[]
	for item in items:
		if items[item]>=support_count(i,j):
			fi.append(item)
		else:
			nfi.append(item)
	print('frequent item sets are:', fi)
	print('non frequent item sets are:', nfi)
	l=len(fi)
	combination(fi,nfi,l)				
	return(fi,nfi,l)
i=int(input('Required Suport:'))
j=int(input('No of Transactions:'))
a=twoset_combination(frequent1_items(Unique_one_count(Unique_one())))
count_candidate_items(a)
