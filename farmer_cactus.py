import u
import plots
import algos

CACTUS_LINE_SIZE = get_world_size()

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

def run():
	quick_print("Farming cactus")
	
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
	
	quick_print(state)
	quick_print(sorted_state)

	# Move the cactuses around to meet the spec
	min_index = 0
	max_index = CACTUS_LINE_SIZE - 1

	u.go_to_plot((0, 0))
	while min_index < max_index:
		grabbed = False
		# Scan through and grab max
		for i in range(max_index - min_index):
			if grabbed or measure() == sorted_state[max_index]:
				swap(East)
				grabbed = True
			move(East)
		max_index = max_index - 1
		move(West)
		grabbed = False
		# Scan through and grab min
		for i in range(max_index - min_index):
			if grabbed or measure() == sorted_state[min_index]:
				swap(West)
				grabbed = True
			move(West)
		min_index = min_index + 1
		move(East)

	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
