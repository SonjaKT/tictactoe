from tictacto import *


a = ['X', 'X', 'X']
b = ['O', 'O', 'X']
c = ['X', 'X', 'O']
a1 = [a, b, c]
# x wins - column
d = ['X', 'X', 'O']
e = ['X', 'O', 'X']
f = ['X', 'X', 'O']
a2 = [d, e, f]

#x wins - diag
g = ['X', 'X', 'O']
h = ['O', 'X', 'O']
i = ['X', 'O', 'X']
a3 = [g,h,i]

#x wins - make sure little x works
j = ['X', 'X', 'x']
k = ['O', 'X', 'O']
l = ['X', 'O', 'X']
a4 = [j,k,l]

# nobody wins
gg = ['X', 'O', 'X']
hh = ['O', 'X', 'O']
ii = ['o', 'X', 'O']
a5 = [gg, hh, ii]

# 'O' wins
gg = ['O', 'O', 'O']
hh = ['O', 'X', 'O']
ii = ['X', 'O', 'X']
a7 = [gg, hh, ii]

# 2 wins
gi = ['X', 'X', 'X']
hi = ['O', 'o', 'O']
ii2 = ['X', 'X', 'X']
a6 = [gi, hi, ii2]

def test_column():
	assert (WhoWin(a1) == 'x'), "Output should be 'X' - rows don't work"

def test_row():
	assert (WhoWin(a2) == 'x'), "Output should be 'X' - columns don't work"

def test_diag():
	assert (WhoWin(a3) == 'x'), "Output should be 'X' - diagonals "

def test_lowercase():
	assert (WhoWin(a4) == 'x'), "Output should be 'X'"

def test_no_wins():
	assert (WhoWin(a5) == None), "Output should be 'None'"

def test_capitalO_wins():
	assert (WhoWin(a7) == 'o'), "Output should be 'O'"

def test_two_wins():
	assert (WhoWin(a6) == None), "Output should be None"

test_column()
test_row()
test_diag()
test_lowercase()
test_no_wins()
test_capitalO_wins()
test_two_wins()


