# Inserts an item into a list using a binary search algorithm
# The comparison function should return the difference of two elements
def binary_insert(list, element, comparison_function):
	if len(list) == 0:
		list.append(element)
		return
	
	left = 0
	right = len(list)
	
	# Binary search to find the insertion position
	while left < right:
		mid = (left + right) // 2
		if comparison_function(element, list[mid]) < 0:
			right = mid
		else:
			left = mid + 1
	
	list.insert(left, element)