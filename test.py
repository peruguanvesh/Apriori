import itertools
import pdb
import re
import os


def readingcodes(name):
  '''Reading the Codes.txt file and returning the list of codes and dictionary with keys as items and values as codes'''
  with open(name,'r') as f:
    dict_itemcodes = {}
    list_codes = []
    for line in f:
      new = line.strip('\n').split(' ')
      dict_itemcodes[new[1]]= new[0]
      list_codes.append(new[0])
  return dict_itemcodes,list_codes


def readingdirty(dict_itemcodes,list_codes,name1):
  '''Cleaning the dirt.txt file and writing the codes of the items in new.txt file'''
  with open(name1,'r') as f:
    for line in f:
      new = line.strip('\n').replace(' ',';').split(';')
      for item in new:
        if item in dict_itemcodes:
          with open('clean.txt','a') as f:
            f.write('{} '.format(dict_itemcodes[item]))
        elif item in list_codes:
          with open('clean.txt','a') as f:
            f.write('{} '.format(item))
        else:
          for k in dict_itemcodes:
            if k in item:
              item=re.sub(k,'',item)
              with open('clean.txt','a') as f:
                f.write('{} '.format(dict_itemcodes[k]))
          if len(item)!=0:
            for j in dict_itemcodes:
              if item in j:
                with open('clean.txt','a') as f:
                  f.write('{} '.format(dict_itemcodes[j]))
                break
      with open('clean.txt','a') as f:
        f.write('\n')

  return dict_itemcodes


#def support_count(support,transactions_count):
#	support_count=(support/100)*transactions_count
#	if support_count is int:
#		return(support_count)
#	else:
#		return(int(support_count)+1)

#f=open('transactions.txt','r')

def Unique_one():
    #f = open(name,'r')
    unique_one=[]
    with open('clean.txt','r') as f:
        for line in f:
            stri=line.strip('\n')
            spli=stri.split(' ')
            del spli[-1]
            for a in spli:
                if a not in unique_one:
                    unique_one.append(a)
	#print('Unique items are:', unique_one)
    return(unique_one)

def Unique_one_count(unique_one):
    unique_one_count={}
    for item in unique_one:
        with open('clean.txt','r') as f:
            count=0
            for line in f:
                stri=line.strip('\n')
                spli=stri.split(' ')
                del spli[-1]
                if (item in spli)==True:
                    count=count+1
            unique_one_count[item]=count
	#print('count of unique items:', unique_one_count)
    return(unique_one_count)

def frequent1_items(unique_one_count,output,min_support):
    f1=[]
    for item in unique_one_count:
        if unique_one_count[item]>=min_support:
            f1.append(item)
    with open(output,'a') as f:
        for i in f1:
            f.write('{}\n'.format(i))
    return(f1)

def twoset_combination(frequent_item):
	twoset_combination=[]
	for twoset in itertools.combinations(frequent_item,2):
		twoset_combination.append(twoset)
	return(twoset_combination)

def combination(fi,nfi,l,output1,min_support):
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
		#print('the candidate combinations are:', combination_tupl)
		count_candidate_items(combination_tupl,output1,min_support)
	return(combination_tupl)

def count_candidate_items(combinations,output1,min_support):
    items={}
    for element in combinations:
        count=0
        with open('clean.txt','r') as f:
            for line in f.readlines():
                stri=line.strip('\n')
                spli=stri.split(' ')
                del spli[-1]
                if len(set(element))==len(set(element)&set(spli)):
                    count=count+1
            items[element]=count
	#print('count of candidate items:', items)
    frequent_items(items,output1,min_support)
    return(items)
nfi=[]
def frequent_items(items,output1,min_support):
    fi=[]
    for item in items:
        if items[item]>=min_support:
            fi.append(item)
        else:
            nfi.append(item)
	#print('frequent item sets are:', fi)
    with open(output1,'a') as f:
        for i in fi:
            f.write('{}\n'.format(i))
	#print('non frequent item sets are:', nfi)
    l=len(fi)
    combination(fi,nfi,l,output1,min_support)
    return(fi,nfi,l)

def main(name1,name2,i,name3):
    dict_itemcodes,list_codes = readingcodes(name2)
    readingdirty(dict_itemcodes,list_codes,name1)
    count_candidate_items(twoset_combination(frequent1_items(Unique_one_count(Unique_one()),name3,min_support=i)),name3,min_support=i)

main('dirty.txt','codes.txt',2,'output1.txt')
os.remove('clean.txt')
main('dirty.txt','codes.txt',5,'output2.txt')
os.remove('clean.txt')
main('dirty.txt','codes.txt',8,'output3.txt')
os.remove('clean.txt')
