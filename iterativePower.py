def iterativePower(x,p):
	result = 1
	for turn in range(p):
		result = turn ** x
    		print('iteration:' + str(turn + 1)+ ' current result:' + str(result))
	return result

iterativePower(2,4)
