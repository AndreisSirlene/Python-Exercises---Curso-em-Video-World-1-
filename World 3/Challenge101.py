def count(i, e, w):  
	"""
	-> Do a count and show in the screen.
	:parameter i: initial of the count
	:parameter e: end of the count
	:parameterw: walk of the count
	"""
	count = i
	while count <= e:    
		print(f'{count}',end='..')
		count += w     # increment
	print('End!')

count(2, 20, 4)