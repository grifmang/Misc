end = 100
start = 0
answer = start + end / 2
guess = 0

print 'Think of a number between 0-100.'
guess = raw_input('Is your number 50? -h-igher or -l-ower, -c-orrect: ')

while guess != 'c':
	if guess == 'l':
		end = answer
		answer = (start + end) / 2
	elif guess == 'h':
		start = answer
		answer = (start + end) / 2
	else:
		print 'Please only choose -h- for Higher, -l- for Lower, or -c- for Correct.'
	guess = raw_input('Is ' + str(answer) + ' your number? -h-igher or -l-ower, -c-orrect: ')

print 'Game Over. Your secret number was ' + str(answer) + '.'
