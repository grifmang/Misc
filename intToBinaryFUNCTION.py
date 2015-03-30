def make_binary(x):
	if x >= 0:
		print bin(x)
		return bin(x)
	elif x < 0:
		print '-' + bin(abs(x))
		return '-' + bin(abs(x))

make_binary(-8)
