import u
import plots
import algos

CACTUS_LINE_SIZE = get_world_size()

# Cactus takes 1 second to grow

def setup():
	quick_print("Setting up cactus farmer")
	change_hat(Hats.Cactus_Hat)
	clear()

def slide(x, length, direction):
	u.go_to(x, 0)
	for i in range(length-1):
		swap(direction)
		move(direction)
	swap(direction)


def run():
	quick_print("Farming cactus")
	
	# TODO make this 2D

	state = []

	# Plant and measure
	for i in range(CACTUS_LINE_SIZE):
		u.go_to_plot((i, 0))
		harvest()
		u.safe_plant(Entities.Cactus)
		size = measure()
		state.append(size)
		
	quick_print("initial state:", state)
	quick_print("")
	
	inversions = u.fill(0, CACTUS_LINE_SIZE)
	
	for i in range(CACTUS_LINE_SIZE):
		for j in range(i, CACTUS_LINE_SIZE):
			if state[j] < state[i]:
				inversions[j] = inversions[j] + 1
				
	quick_print("inversions", inversions)

	for i in range(CACTUS_LINE_SIZE):
		if inversions[i] != 0:
			slide(i, inversions[i], West)

	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
