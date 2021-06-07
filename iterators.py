from itertools import product
a = [1,2]

b = [3]

prod = product(a,biter1)

print("Give cross product  : ",list(prod))
a = [1,2]

b = [3]
prod = product(a,b, repeat=2)
print(list(prod))



print("******************************************************************")

from itertools import permutations
a = [1,2,3]

perm = permutations(a)
print("Permutauions ", list(perm))

perm = permutations(a , 2)
print(list(perm))


print("******************************************************************")

from itertools import combinations , combinations_with_replacement

a = [1,2,3,4]
comb = combinations(a, 2)
print("nCr ",list(comb))

comb_wr = combinations_with_replacement(a,2)
print("nCr with replacement",list(comb_wr))

print("******************************************************************")

from itertools import accumulate
import operator
a = [1,2,3,4]

acc = accumulate(a)

print(a)
print(list(acc))  #by default calculate the sum upto that element

acc = accumulate(a , func = max)

print(a)
print(list(acc))



print("******************************************************************")

from itertools import groupby
a = [1,2,3,4]

def smaller(x):
	return x < 3 

#group_obj = groupby(a , key=smaller)
group_obj = groupby(a , key=lambda x : x < 3)

for key,value in group_obj:
	print(key , list(value))


print("*******************************************************************")

from itertools import count, cycle, repeat

for i in count(10):  #count from 10 to infinity
	print(i)
	if i == 15:
		break

num = 1
a = [1,2,3]  #repeat a infinite times
for i in cycle(a):
	print(i)
	if(num == 6):
		break
	num += 1


a = [1,2,3]
for i in repeat(1, 4):  #repeat i i.e. 1 for 4 time else infitine times
	print(i)