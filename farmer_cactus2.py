import u
import plots
import algos

cactus_plots = plots.get_all_plots_alternating()
size_per_plot = 9 / 9


# Cactus takes 1 second to grow

def setup():
	quick_print("Setting up cactus farmer")
	change_hat(Hats.Cactus_Hat)
	
	clear()
	for plot in cactus_plots:
		u.go_to_plot(plot)
		till()

def slide(x, length, direction):
	#quick_print("sliding x:", x, " length:", length)
	u.go_to(x, 0)
	for i in range(length-1):
		swap(direction)
		move(direction)
	swap(direction)


def run():
	quick_print("Farming cactus")
	
	for x, y in cactus_plots:
		u.go_to(x, y)
		plant(Entities.Cactus)
		target_size = x * size_per_plot
		while measure() != 9:
			harvest()
			plant(Entities.Cactus)
	end = get_time()
	
	while (get_time() - end) < 2:
		do_a_flip()

	harvest()

		
if __name__ == "__main__":
	setup()
	while True:
		run()
		