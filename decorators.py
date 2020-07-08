def start_end_decorator(func):

	def wrapper():
		print('Start')
		func()
		print('End')

	return wrapper

@start_end_decorator
def print_name():
	print("Tanej")


print_name()  # if we want to give arguments we have to give in all the functions at the top

print("**************************************************************")


def start_end_decorator(func):

	def wrapper(*args, **kwargs):
		print('Start')
		result = func(*args, **kwargs)
		print('End')
		return result
	return wrapper

@start_end_decorator
def print_name(a, b):
	print(a*b)

print(print_name(2,4))