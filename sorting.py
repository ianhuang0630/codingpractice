import heapq

class Sort:
	def __init__ (self, input_list, ascending = True):
		self.list = input_list
		self.ascending = ascending

	def compare(self, a, b):
	
		if a < b:
			return int(self.ascending)
		if a == b:
			return 0
		return -int(self.ascending)

	def bubblesort(self):

		for i in range(len(self.list)):
			for j in range(len(self.list)-1):
				# comparing jth element to j+1th element
				if self.compare(self.list[j], self.list[j+1]) == -1:
					self.list[j], self.list[j+1] = self.list[j+1], self.list[j]

		return self.list

	def insertionsort(self):
		for i in range(1, len(self.list)):
			j = i
			while j > 0:
				# comparing j and j-1
				if self.compare(self.list[j-1], self.list[j]) != 1:
					self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
					j -= 1
				else:
					break

		return self.list

	def mergesort(self):
		
		if len(self.list) == 1:
			return self.list

		mid_length = len(self.list)//2

		first_portion = Sort(self.list[:mid_length]).mergesort()
		second_portion = Sort(self.list[mid_length:]).mergesort()

		import ipdb; ipdb.set_trace()
		# merging:
		merged = []
		first, second = 0,0
		while first != len(first_portion) and second != len(second_portion):
			# compare the corresponding element in both lists
			temp = self.compare(first_portion[first], second_portion[second])
			if temp != -1:
				merged.append(first_portion[first])
				first += 1
			elif temp == -1:
				merged.append(second_portion[second])
				second += 1

		merged += first_portion[first:] + second_portion[second:]
		first, second = len(first_portion), len(second_portion)

		self.list = merged

		return self.list

	def heapsort(self):

		if self.ascending:
			heapq.heapify(self.list)
		else:
			heapq._heapify_max(self.list)

		return self.list

	def quicksort(self):

		if len(self.list) <= 1:
			return self.list

		mid_length = len(self.list)//2
		left = []
		middle_el = self.list[mid_length]
		right = []

		for i in range(len(self.list)):
			if self.compare(self.list[i], middle_el) != -1 and i != mid_length:
				# move i before mid_length:
				left.append(self.list[i])

			elif self.compare(self.list[i], middle_el) == -1 and i != mid_length:
				# move i after mid_length
				right.append(self.list[i])

		self.list = Sort(left).quicksort() + [middle_el] + Sort(right).quicksort()

		return self.list

def main():
	a = [2,5,3,1]

	sort = Sort(a)
	print(sort.quicksort())

if __name__=="__main__":
	main()


