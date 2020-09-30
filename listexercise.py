#program for printing all the even numbers in a list of numbers with list comprehension 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a1 = [i for i in a if i%2==0]
print (a1)

#Use below to do the above without list comprehension 
#for i in a:
#	if i%2==0:
#		a1.append(i)

#print(a1)

