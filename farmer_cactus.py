import u
import plots
import algos

cactus_plots = plots.get_plots_alternating(0, 0, 10, 1)

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
	for i in range(10):
		u.go_to_plot((i, 0))
		harvest()
		u.safe_plant(Entities.Cactus)
		size = measure()
		algos.binary_insert(sorted_state, size, number_comp)
		state.append(size)
	
	quick_print(state)
	quick_print(sorted_state)

	# Move the cactuses around to meet the spec
	for i in range(10):
		plot = (i, 0)
		u.go_to_plot(plot)
		
		if measure() != sorted_state[i]:
			count = 0
			# Scan for the right size and bring it back
			while measure() != sorted_state[i]:
				move(East)
				count = count + 1
			for ii in range(count):
				swap(West)
				move(West)

	u.go_to_plot((0, 0))
	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
