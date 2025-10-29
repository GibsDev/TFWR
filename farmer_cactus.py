import u
import plots
import algos

CACTUS_LINE_SIZE = 7

# Cactus takes 1 second to grow

def setup():
	quick_print("Setting up cactus farmer")
	change_hat(Hats.Cactus_Hat)
	clear()

def left_swap(state):
	swap(West)
	tmp = state[len(state) - 2]
	state[len(state) - 2] = state[len(state) - 1]
	state[len(state) - 1] = tmp

def number_comp(a, b):
	return a - b

def do_sort():
	sorted = True
	if measure(West) > measure():
		swap(West)
		sorted = False
	if measure(East) < measure():
		swap(East)
		sorted = False
	return sorted

def run():
	quick_print("Farming cactus")
	
	# TODO make this 2D

	state = []
	sorted_state = []

	# Plant and measure
	for i in range(CACTUS_LINE_SIZE):
		u.go_to_plot((i, 0))
		harvest()
		u.safe_plant(Entities.Cactus)
		size = measure()
		algos.binary_insert(sorted_state, size, number_comp)
		state.append(size)
		
	quick_print("initial state:", state)
	quick_print("target state:", sorted_state)
	quick_print("")
	
	# TODO implement algo

	index_lookup = {}
	# Insert empty arrays for all possible cactus values
	for i in range(10):
		index_lookup[i] = []
	# Build the lookup
	for i in range(len(sorted_state)):
		algos.binary_insert(index_lookup[sorted_state[i]], i, number_comp)

	# index_lookup should now look like:
	# {1: [0, 1, 2], 2: [3], 3: [4, 5], 4: [5]}
	# For sorted_state: [1, 1, 1, 2, 3, 3, 4]

	quick_print("index_lookup", index_lookup)

	# use the sorted list to calculate the deltas for the slots
	deltas = []
	for i in range(len(state)):
		value = state[i]
		indexes_for_current_value = index_lookup[value]
		min_index = indexes_for_current_value[0]
		max_index = indexes_for_current_value[-1]
		delta = 0
		if i >= min_index and i <= max_index:
			delta = 0
		else:
			# Find the smallest delta max vs min
			min_delta = min_index - i
			max_delta = max_index - i
			if abs(min_delta) < abs(max_delta):
				delta = min_delta
			else:
				delta = max_delta
		deltas.append(delta)

	quick_print("deltas", deltas)

	# TODO virtually simulate the swapping algorithm
	# and record steps so we can play them back

	current_index = 9

	# TODO repeat swapping algorithm until all deltas are 0
	# how can we efficiently check that? Keep a running tally?

	# helper function for performing swaps by keeping track of state
	def do_swap():
		# TODO perform swaps and keep track of state

	# Get the nearest delta that is not 0 and perform the swap
	# swap in the direction of the delta value
	# increment or decrement any non 0 passed values accordingly
	# keep an eye out for running into finished (0 delta) cactuses of the same size and stop early







	# # Move the cactuses around to meet the spec
	# min_index = 0
	# max_index = CACTUS_LINE_SIZE - 1

	# u.go_to_plot((0, 0))
	# while min_index < max_index:
	# 	while measure() == sorted_state[get_pos_x()] and get_pos_x() < max_index:
	# 		move(East)
	# 		min_index = min_index + 1
	# 	# Scan through and grab max
	# 	for i in range(max_index - min_index):
	# 		if measure() == sorted_state[max_index]:
	# 			# "grab" the size we need for the end
	# 			swap(East)
	# 		else:
	# 			do_sort()
	# 		move(East)
	# 	max_index = max_index - 1
	# 	move(West)
	# 	while measure() == sorted_state[get_pos_x()] and get_pos_x() > min_index:
	# 		move(West)
	# 		max_index = max_index - 1
	# 	# Scan through and grab min
	# 	for i in range(max_index - min_index):
	# 		if measure() == sorted_state[min_index]:
	# 			# "grab" the size we need for the end
	# 			swap(West)
	# 		else:
	# 			do_sort()
	# 		move(West)
	# 	min_index = min_index + 1
	# 	move(East)

	while True:
		do_a_flip()

	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
