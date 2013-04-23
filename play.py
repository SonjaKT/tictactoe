from tictacto import WhoWin
from random import randint, randrange
from play2 import look_for_2s

L = [['_','_','_'],['_','_','_'],[' ',' ',' ']]
D = {'UL':(0,0), 'UM':(0,1), 'UR':(0,2), 'ML':(1,0), 'MM':(1,1), 'MR':(1,2), 'LL':(2,0), 'LM':(2,1), 'LR':(2,2)}

def f(x):
	if 2 in x:
		print 'zoo'
	elif 4 in x:
		return 'humbug'
	if 3 in x:
		return 'bar'
	return 'baz'

def find_corners(L):
	if L[0][0] == 'o' and (L[2][2]=='_' or L[2][2]==' '): 
		L[2][2] = 'o' 
		return L, True
	if L[0][2] == 'o' and (L[2][0]=='_' or L[2][0]==' '): 
		L[2][0] = 'o' 
		return L, True
	if L[2][0] == 'o' and (L[0][2]=='_' or L[0][2]==' '): 
		L[0][2] = 'o' 
		return L, True
	if L[2][2] == 'o' and (L[0][0]=='_' or L[0][0]==' '): 
		L[0][0] = 'o' 
		return L, True
	else: return L, False

def find_edges(L):
	if L[0][1] =='_' or L[0][1] =='_': 
		L[0][1] ='o' 
		return L, True
	if L[1][0] =='_' or L[1][0] =='_': 
		L[1][0] ='o' 
		return L, True
	if L[1][2] =='_' or L[1][2] =='_': 
		L[1][2] ='o' 
		return L, True
	if L[2][1] =='_' or L[2][1] =='_': 
		L[2][1] ='o' 
		return L, True
	else: return L, False

def print_current_board(L):
	print "_%s_|_%s_|_%s_" % (L[0][0],L[0][1],L[0][2])
	print "_%s_|_%s_|_%s_" % (L[1][0],L[1][1],L[1][2])
	print " %s | %s | %s " % (L[2][0],L[2][1],L[2][2])

def next_move(L):
	a,b=randint(0,2),randint(0,2)
	while (not L[a][b]=='_') and (not L[a][b]==' '):
		a,b=randint(0,2),randint(0,2)
	L[a][b]='o'
	return L

def first_move(L,m1):
	if m1 == 'MM':
		a,b= randrange(0,3,2), randrange(0,3,2)
		while (not L[a][b]=='_') and (not L[a][b]==' '):
			a,b = randrange(0,3,2), randrange(0,3,2)
		L[a][b]='o'
	else: L[1][1]='o'
	return L

def next_move_H(L):
	if look_for_2s(L,'o')[1]: 
		return L #finish the game
	if look_for_2s(L,'x')[1]: 
		return L #block
	if find_corners(L)[1]: 
		return L #place an o in the best corner
	else: 
		return find_edges(L)[0]

def make_move(L,m): # m is a string, D[m] is the tuple of numbers associated with it
	if L[D[m][0]][D[m][1]]=='_' or L[D[m][0]][D[m][1]]==' ':
		L[D[m][0]][D[m][1]]='x'
		return L
	else:
		n = raw_input("that spot's taken! try again: ")
		return make_move(L,n)

def solicit_move(L):
	m = raw_input("next_move: ")
	return make_move(L,m)

def play():
	print "Hello, play with me"
	print_current_board(L)
	m1 = raw_input("what is your first move? (enter UL,UM,UR,ML,MM,MR,LL,LM or LL) ")
	print_current_board(make_move(L,m1)) #prints the board after the person moves
	print_current_board(first_move(L,m1)) #prints the board after the computer moves
	i = 0
	while i<8:
		if i%2 == 0: board = solicit_move(L)
		else: board = next_move_H(L)
		print_current_board(board) 
		if WhoWin(L)[0]: 
			i = 9
			print WhoWin(L)[1]
		else: 
			i=i+1
	return 0

if __name__=="__main__":
	play()
