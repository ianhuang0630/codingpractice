# class Solution(object):
# 	def longestPalindrome(self, s):
# 		longest = ""

# 		for i in range(len(s)-1):
# 			for j in range(i, len(s)):
# 				if s[i:j+1] == s[i:j+1][::-1] and j-i > len(longest):
# 					longest = s[i:j+1]

# 		return longest


class Solution(object):
	def longestPalindrome(self, s):
		
		max_pal = [0,0]

		odd = {}
		odd = {index: [index, index] for index in range(len(s))}

		cont = True
		while cont:
			cont = False
			# check for every key in odd that odd[key][0]-1 and odd[key][1]+1 
			for i in odd.keys():
				if odd[i][0]-1 >= 0 and odd[i][1]+1 < len(s):

					if s[odd[i][0]-1] == s[odd[i][1]+1]:
						# then it is a palendrome -- adjust the margins
						odd[i][0] -= 1
						odd[i][1] += 1
						cont = True

				if odd[i][1]-odd[i][0] > max_pal[1]-max_pal[0]:
					max_pal = odd[i]

		even = {}
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				even[i] = [i, i+1]

		# TODO: intialize even
		cont = True
		while cont:
			cont = False

			for i in even.keys():
				if even[i][0]-1 >= 0 and even[i][1]+1 <len(s):
					if s[even[i][0]-1] == s[even[i][1]+1]:
						even[i][0] -=1
						even[i][1] += 1
						cont = True
				if even[i][1]-even[i][0] > max_pal[1]-max_pal[0]:
						max_pal = even[i]

		return s[max_pal[0]:max_pal[1]+1]

	def islandPerimeter(self, grid):
		"""
		Inputs:
			grid (list of lists): grid
		"""
		# visited = [[0]*len(grid[0])]*len(grid)

		def add_perim(position):
			"""
			Inputs:
				position (list): position on island
			Returns:
				perim (int): 4 if alone, 3 if surrounded by water on 3
					sides, 2 if surrounded by water on 2 sides..etc
			"""


			tries = [[-1,0],[1,0],[0,-1],[0,1]]

			perim = 0
			for pair in tries:

				if position[0]+pair[0] >= len(grid):
					perim += 1
				elif position[0]+pair[0] < 0:
					perim += 1
				elif position[1]+pair[1] >= len(grid[0]):
					perim += 1
				elif position[1]+pair[1] < 0:
					perim += 1
				elif grid[position[0]+pair[0]][position[1]+pair[1]] == 0:
					perim += 1

			return perim

		perim = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j]:
					perim += add_perim([i,j])

		return perim


def main():
	sol = Solution()
	test = "bb"
	import ipdb; ipdb.set_trace()

	print(sol.longestPalindrome(test))


if __name__ == "__main__":
	main()

