"""
def TTTW(L,n=3,x=3):
	for i in L:
		if sum(i) == x: return True 
		else: pass
	if sum([L[i][i] for i in range(n)]) == x: return True
	else: pass
	if sum([L[i][n-i-1] for i in range(n)]) == x: return True 	
	for j in range(n):
		if sum([L[i][j] for i in range(n)]) == x: return True
		else: pass
	return False

def convert(L):
	L2 = []
	n = len(L)
	ty = type(L[0][0])
	for i in L: 
		if len(i) != n: raise Exception("L is not a square")
		for j in i:
			if not isinstance(j, ty): raise Exception("get your tipes rite, dummy")
	if ty == str:
		for j in range(n):
			L2.append([L[j][i].lower() for i in range(n)])
		for i in L2: 
			for j in range(n):
				if i[j] == "x": i[j] = 1
				elif i[j] == "o": i[j] = 0
				else: raise Exception("what are these other letters?")
	elif ty == int:
		for i in L:
			for j in range(n):
				if i[j]>=0: pass
				else: raise Exception("negative numbers, wtf")
		for j in range(n):
			L2.append([L[j][i]%2 for i in range(n)])
	elif ty == bool:
		for j in range(n):
			L2.append([1 if L[j][i] else 0 for i in range(n)])
	else: raise Exception("I accept matrices of type integers, boolians, or xs and os")
	return L2,n	
"""
def convert(L):
	n = len(L)
	L2=[[],[],[]]
	for i in range(n): 
		for j in range(n):
			if L[i][j] == "x" or L[i][j] == "1" : L2[i].append(+1)
			if L[i][j] == "o" or L[i][j] == "-1" : L2[i].append(-1)
			if L[i][j] == " " or L[i][j] == "_" or L[i][j] == 0: L2[i].append(0)
	return L2,n

def TTTW(L,n=3,x=-3):
	for i in L:
		if sum(i) == x: return True 
	if sum([L[i][i] for i in range(n)]) == x: return True
	if sum([L[i][2-i] for i in range(n)]) == x: return True 	
	for j in range(n):
		if sum([L[i][j] for i in range(n)]) == x: return True
	return False
	

def WhoWin(L):
	L,n = convert(L)
	if TTTW(L,3,3) and (not TTTW(L,n,-3)): return True, 'x wins!!'
	if (not TTTW(L,3,3)) and TTTW(L,n,-3): return True, 'o wins!!'
	game_over = True	
	for i in range(3):
		for j in range(3):
			if L[i][j] == 0: game_over = False
	return game_over, 'no one wins, draw, play again'
