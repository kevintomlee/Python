import random

class Board:
	''' N by N slider puzzle
	'''
	Direction = ('UP', 
				 'DOWN',
				 'LEFT',
				 'RIGHT')

	def __init__(self, n=3, tiles=None):
		if tiles!=None:
			self.block = []
			for i in range(len(tiles)):
				if tiles[i] == 0:
					self.freeTile = i
				self.block.append(tiles[i])
			import math
			self.N = int(math.sqrt(len(tiles)))
		else:
			self.N = n
			self.freeTile = n*n -1
			self.block, self.freeTile = self.genRanSeq()

	def genRanSeq(self, s=1):
		sequence = []
		newseq = []
		length = self.N*self.N
		for i in range(length):
			sequence.append(i)
			newseq.append(0)
		seqrange = length
		random.seed(s)
		freetileidx = 0
		for i in range(length):
			e = random.randrange(seqrange)
			newseq[i] = sequence[e]
			if newseq[i]==0:
				freetileidx = i
			sequence[seqrange-1], sequence[e] = sequence[e], sequence[seqrange-1]
			seqrange -= 1
		return newseq, freetileidx


	def getXY(self, index):
		x = index // self.N
		y = index %  self.N
		return x, y

	def getIndex(self, x, y):
		return x*self.N + y

	def hamming(self):
		res = 0
		for i in range(len(self.block)-1):
			if i+1 != self.block[i]:
				res += 1
		return res

	def manhattan(self):
		res = 0
		for i in range(len(self.block)):
			if self.block[i]!=0:
				x1, y1 = self.getXY(i)
				x2, y2 = self.getXY(self.block[i]-1)
				dif = abs(x1-x2) + abs(y1-y2)
				res += dif
		return res

	def __eq__(self, other):
		if isinstance(other, Board):
			if len(self.block) == len(other.block):
				for i in range(len(self.block)):
					if self.block[i]!=other.block[i]:
						return False
				return True
		return False

	def neighbors(self):
		n = []
		for d in self.Direction:
			b = Board(tiles=self.block)
			b.move(d)
			if self != b:
				n.append(b)
		return n

	def move(self, direction):
		x, y = self.getXY(self.freeTile)
		oldidx = self.getIndex(x, y)
		if direction==self.Direction[0]:
			newidx = self.getIndex(x-1, y)
			if x-1 not in range(self.N):
				return False
			self.block[oldidx], self.block[newidx] = self.block[newidx], self.block[oldidx]
			self.freeTile = newidx
			return True
		elif direction==self.Direction[1]:
			newidx = self.getIndex(x+1, y)
			if x+1 not in range(self.N):
				return False
			self.block[oldidx], self.block[newidx] = self.block[newidx], self.block[oldidx]
			self.freeTile = newidx
			return True
		elif direction==self.Direction[2]:
			newidx = self.getIndex(x, y-1)
			if y-1 not in range(self.N):
				return False
			self.block[oldidx], self.block[newidx] = self.block[newidx], self.block[oldidx]
			self.freeTile = newidx
		elif direction==self.Direction[3]:
			newidx = self.getIndex(x, y+1)
			if y+1 not in range(self.N):
				return False
			self.block[oldidx], self.block[newidx] = self.block[newidx], self.block[oldidx]
			self.freeTile = newidx
		return False

	def __str__(self):
		result = []
		for i in range(self.N):
			for j in range(self.N):
				if self.block[self.getIndex(i,j)]==0:
					result.append('_')
				else:
					result.append(str(self.block[self.getIndex(i,j)]))
			result.append('\n')
		return ''.join(result)

if __name__ == '__main__' :
	N = 3
	board = Board(N)
	print(board)
	a = input('move:')
	while a!='q':
		if a == 'q':
			break
		if a == 'u':
			board.move('DOWN')
		if a == 'd':
			board.move('UP')
		if a == 'r':
			board.move('LEFT')
		if a == 'l':
			board.move('RIGHT')
		print(board)
		a = input('move:')
