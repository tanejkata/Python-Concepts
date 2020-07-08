from collections import Counter

a = "aaaabbbbbbbvcccccccc"

my_counter = Counter(a)

print(my_counter)

print("All Items in my counter " , my_counter.items())

print("All my keys in counter ",my_counter.keys())

print("All my item values in counter ",my_counter.values())


n = 1
print("Most common elements where n is the how many top most elements",my_counter.most_common(n))

print("iterator along the string elements",list(my_counter.elements()))


print("*******************************************************************************************")


from collections import namedtuple

point = namedtuple('point','x,y')

pt = point(1,5)

print(pt)
print(pt.x , pt.y)

print("*******************************************************************************************")

from collections import  defaultdict

d = defaultdict(int)   #here we can give default value for the keys if not present
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d['d'])


print("*******************************************************************************************")


from collections import deque

d = deque()  #here we can do operation on left or right

d.append(1)
d.append(2)

print(d)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extendleft([4,5,6])
print(d)


d.rotate(-1)
print(d)