x = -5
'''
if x < 0:
	raise Exception('x should be positive')

x = -5
assert (x >= 0) , 'x is not positive'

try:
	a = 5/0
except Exception as e:
	print(e)
print("**************************************************")
try:
	a = 5 / 0
	b = a + 'a'
except ZeroDivisionError as e:
	print(e)
except TypeError as e:
	print(e)
else:
	print("everthing is fine")
finally:
	print("cleaning up....")

	
class ValueToolHighError(Exception):
	pass


def test_value(x):
	if x > 100:
		raise ValueToolHighError('value is too high')

try:
	test_value(200)
except ValueToolHighError as e:
	print(e)

'''

def mygenerator():
	yield 1
	yield 2
	yield 3

g = mygenerator()

value = next(g)
print(value)

value = next(g)
print(value)