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


	def findMinDifference(self, timepoints):
		"""
		:type timePoints: List[str]
		:rtype: int
		""" 

		def convert_mins(str_time):
			time = str_time.split(":")
			return int(time[0]) * 60 + int(time[1])

		def merge_sort(arr):

			if len(arr) > 1:
				mid_index = len(arr)//2
				left = merge_sort(arr[:mid_index])
				right = merge_sort(arr[mid_index:])

				# merging left and right
				left_i, right_i = 0, 0
				sort = []

				while left_i < len(left) and right_i < len(right):
					if left[left_i] <= right[right_i]:
						sort.append(left[left_i])
						left_i += 1
					else:
						sort.append(right[right_i])
						right_i += 1

				sort += left[left_i:] + right[right_i:]

				return sort

			
			return arr

		def time_diff(mins_1, mins_2):
			"""
			mins_1 > mins_2
			"""
			return min(mins_1 - mins_2, 24*60-mins_1 + mins_2)

		mins_list = [convert_mins(element) for element in timepoints]
		mins_list_sorted = merge_sort(mins_list)

		minimum_delt = float("inf")

		for i in range(len(mins_list_sorted) - 1):
			# i+1 and i

			delt = time_diff(mins_list_sorted[i+1], mins_list_sorted[i])

			if delt < minimum_delt:
				minimum_delt = delt

		minimum_delt = min(minimum_delt, time_diff(mins_list_sorted[-1], mins_list_sorted[0]))

		return minimum_delt

	def maxArea(self, height):

		# move left and right in the array given the middle two elements. 

		middle_index = len(height)//2 -1
		start_min = height[middle_index-1]
		end_min = height[middle_index]

		left = middle_index-1
		right = middle_index

		max_area = (right-left)*min(height[left], height[right])

		while left >= 0 or right < len(height):

			# if left > right, then move right outwards
			if left >= 0 and right < len(height):
				if height[left] > height[right]:
					right += 1
					new_area = (right-left)*min(height[left], height[right])

					max_area = max(new_area, max_area)

				else:
					left -= 1
					new_area = (right-left)*min(height[left], height[right])

					max_area = max(new_area, max_area)
			
			elif right == 0:
				left -= 1
				new_area = (right-left) * min(height[left], height[right])
				max_area = max(new_area, max_area)

			else:
				right += 1
				new_area = (right-left) * min(height[left], height[right])
				max_area = max(new_area, max_area)

		return max_area 


def main():
	sol = Solution()
	test = "bb"
	import ipdb; ipdb.set_trace()

	print(sol.longestPalindrome(test))

	test = ["05:31","22:08","00:35"]
	print(sol.findMinDifference(test))

if __name__ == "__main__":
	main()

