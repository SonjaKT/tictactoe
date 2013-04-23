def look_for_2s(L,s):
	#check rows and columns
	for i in range(3):
		if (L[i][0] == s and L[i][1] == s) and (L[i][2]=='_' or L[i][2]==' '):
			L[i][2] = 'o'
			return L, True
		if (L[i][0] == s and L[i][2] == s) and (L[i][1]=='_' or L[i][1]==' '):
			L[i][1] = 'o'
			return L, True
		if (L[i][1] == s and L[i][2] == s) and (L[i][0]=='_' or L[i][0]==' '):
			L[i][0] = 'o'
			return L, True
		if (L[0][i] == s and L[1][i] == s) and (L[2][i]=='_' or L[2][i]==' '):
			L[2][i] = 'o'
			return L, True
		if (L[0][i] == s and L[2][i] == s) and (L[1][i]=='_' or L[1][i]==' '):
			L[1][i] = 'o'
			return L, True
		if (L[1][i] == s and L[2][i] == s) and (L[0][i]=='_' or L[0][i]==' '):
			L[0][i] = 'o'
			return L, True
	#check diagonals
	if (L[0][0] == s and L[1][1] == s) and (L[2][2]=='_' or L[2][2]==' '):
		L[2][2] = 'o'
		return L, True
	if (L[2][2] == s and L[1][1] == s) and (L[0][0]=='_' or L[0][0]==' '):
		L[0][0] = 'o'
		return L, True
	if ((L[0][0] == s and L[2][2] == s) or (L[0][2] == s and L[2][0] == s))and (L[1][1]=='_' or L[1][1]==' '):
		L[1][1] = 'o'
		return L, True
	if (L[0][2] == s and L[1][1] == s) and (L[2][0]=='_' or L[2][0]==' '):
		L[2][0] = 'o'
		return L, True
	if (L[2][0] == s and L[1][1] == s) and (L[0][2]=='_' or L[0][2]==' '):
		L[0][2] = 'o'
		return L, True
	return L, False

'''
def look_for_2s(L,s):
	if L[1][1] == s:
		for i in range(3):
			if L[0][i] == s and (L[2][2-i]=='_' or L[2][2-i]==' '): 
				L[2][2-i] = 'o'
				return L, True
			if L[2][i] == s and (L[0][i]=='_' or L[0][i]==' '): 
				L[0][i] = 'o'
				return L, True
		if L[1][0] == s and (L[1][2]=='_' or L[1][2]==' '):
			L[1][2] = 'o'
			return L, True
		if L[1][2] == s and (L[1][0]=='_' or L[1][0]==' '):
			L[1][0] = 'o'
			return L, True
	if ((L[0][0] == s and L[0][1] == s) or (L[2][2] == s and L[1][2] == s)) and (L[0][2]=='_' or L[0][2]==' '): 
		L[0][2] ='o' 
		return L, True
	if ((L[2][0] == s and L[1][0] == s) or (L[0][2] == s and L[0][1] == s)) and (L[0][0]=='_' or L[0][0]==' '):
		L[0][0] = 'o'
		return L, True
	if ((L[0][0] == s and L[1][0] == s) or (L[2][2] == s and L[2][1] == s)) and (L[2][0]=='_' or L[2][0]==' '): 
		L[2][0] = 'o' 
		return L, True
	if ((L[2][0] == s and L[2][1] == s) or (L[0][2] == s and L[1][2] == s)) and (L[2][2]=='_' or L[2][2]==' '):
		L[2][2] = 'o'
		return L, True

	if L[0][0] == s and L[0][2] == s and (L[0][1]=='_' or L[0][1]==' '): 
		L[0][1] = 'o' 
		return L, True
	if L[2][0] == s and L[2][2] == s and (L[2][1]=='_' or L[2][1]==' '):
		L[2][1] = 'o'
		return L, True
	if L[2][2] == s and L[0][2] == s and (L[1][2]=='_' or L[1][2]==' '):
		L[1][2] = 'o'
		return L, True
	if L[0][0] == s and L[2][0] == s and (L[1][0]=='_' or L[1][0]==' '):
		L[1][0] = 'o'
		return L, True
	return L, False
'''
