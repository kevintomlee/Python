
class Puzzle:
	''' N by N puzzle
	'''
	Direction = ('UP', 
				 'DOWN',
				 'LEFT',
				 'RIGHT')

	def __init__(self, n):
		self.block = []
		self.N = n
		self.freeTile = n*n-1
		for i in range(n*n-1):
			self.block.append(i+1)
		self.block.append(0)

	def genRanSeq(self):
		pass

	def getXY(self, index):
		x = index // self.N
		y = index %  self.N
		return x, y

	def getIndex(self, x, y):
		return x*self.N + y

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
	grid = Puzzle(N)
	a = input('move:')
	while a!='q':
		if a == 'q':
			break
		if a == 'u':
			grid.move('DOWN')
		if a == 'd':
			grid.move('UP')
		if a == 'r':
			grid.move('LEFT')
		if a == 'l':
			grid.move('RIGHT')
		print(grid)
		a = input('move:')
