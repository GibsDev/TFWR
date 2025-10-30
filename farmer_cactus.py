import u
import plots
import algos

CACTUS_LINE_SIZE = get_world_size()
size_per_plot = 9 / CACTUS_LINE_SIZE
state = []

# Cactus takes 1 second to grow

def setup():
	quick_print("Setting up cactus farmer")
	change_hat(Hats.Cactus_Hat)
	
	clear()
	u.go_to(0, 0)
	for i in range(CACTUS_LINE_SIZE):
		till()
		move(East)

def slide(x, length, direction):
	#quick_print("sliding x:", x, " length:", length)
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
		u.go_to(i, 0)
		plant(Entities.Cactus)
		target_size = i * size_per_plot
		while abs(measure() - target_size) > 2:
			harvest()
			plant(Entities.Cactus)
		state.append(measure())
		
	quick_print("initial state:", state)
	quick_print("")
	
	inversions = u.fill(0, CACTUS_LINE_SIZE)
	
	for i in range(CACTUS_LINE_SIZE):
		for j in range(i, CACTUS_LINE_SIZE):
			if state[j] < state[i]:
				inversions[j] = inversions[j] + 1
				
	quick_print("inversions", inversions)

	blanks = []

	counter_0 = 0
	for i in range(CACTUS_LINE_SIZE):
		blanks.append(counter_0)
		if inversions[i] == 0:
			counter_0 = counter_0 + 1
		else:
			counter_0 = 0
	
	quick_print("blanks    ", blanks)
	
	for i in range(CACTUS_LINE_SIZE -1, -1, -1):
		if inversions[i] != 0 and inversions[i] < blanks[i]:
			slide(i, inversions[i], West)
			inversions[i] = 0

	for i in range(CACTUS_LINE_SIZE):
		if inversions[i] != 0:
			slide(i, inversions[i], West)

	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
