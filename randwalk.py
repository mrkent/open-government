from random import random

def randwalk(n,s=1,s3='good'):
	state = s
	if s3 == 'good':
		p32 = 0.2
		p33 = 0.9
	else: 
		p32 = 0.1
		p33 = 0.8

	path = str(state)
	for i in range(n):
		if state == 1:
			p = random()
			if p <= 0.9: 
				path += str(state)
			else:
				state = 2
				path += str(state)
		elif state == 2:
			p = random()
			if p <= 0.1:
				state = 1
				path += str(state)
			elif p <= 0.9:
				path += str(state)
			else:
				state = 3
				path += str(state)
		elif state == 3:
			p = random()
			if p <= p32:
				state = 2
				path += str(state)
			elif p <= p33:
				path += str(state)
			else:
				state = 4
				path += str(state)
		elif state == 4:
			p = random()
			if p <= 0.6:
				path += str(state)
			else:
				state = 0
				path += str(state)
		else:
			return path
			break
	return path

